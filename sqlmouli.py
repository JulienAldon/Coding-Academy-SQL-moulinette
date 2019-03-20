import sqlalchemy
from sqlalchemy.sql import text
import sys
import difflib
import os

engine = sqlalchemy.create_engine("mysql+pymysql://root:root@localhost:3306/coding")

def executeSql(sta):
	with engine.connect() as con:
		statement = text(sta)
		rs = con.execute(statement)
	return rs

def getSqlStatement(path):
	statement_list = []
	with open(path, 'r') as f:
		statement = f.readlines()
	st = ''.join(statement)
	return (st)

def create_arbo(folder):
	"""Create a List sorted by alphabetical order with the 
		content of the folder given as parameter.
	:param folder: A string containing the folder to list files.
	:rtype: A list of the files in folder.
	"""
	return sorted(os.listdir(folder), key=str.lower)

def what_do_i_correct(reference, test):
	"""Sets list for ref and test
	"""
	folder_reference = reference
	folder_test = test
	arbo_test = create_arbo(folder_test)
	arbo_ref = create_arbo(folder_reference)
	if '.git' in arbo_test:
		arbo_test.remove('.git')
	if 'trace.txt' in arbo_test:
		arbo_test.remove('trace.txt')
	arbo_test = [x for x in arbo_test if x in arbo_ref]
	to_test = [b+'/'+b+'.sql' for b in arbo_test]
	return to_test

def gen_diff(a, b):
	diff = difflib.HtmlDiff().make_file(a,b)
	return diff

# path = "../test/sqltest/ex_19/ex_19.sql"
# for row in executeSql(getSqlStatement(path)):
# 	print(row)


if __name__ == "__main__":
	try:
		ref = sys.argv[1]
		test = sys.argv[2]
		to_correct = what_do_i_correct(ref, test)
	except:
		print("error wrong arguments use -h")
		sys.exit(84)
	result_test = []
	result_ref = []
	for a in to_correct:
		result_ref.append("__________________EXERCICE_"+ a+"__________________")
		res = executeSql(getSqlStatement(ref + a))
		for t in res:
			result_ref.append(str(t))
		try:
			result_test.append("__________________EXERCICE_"+ a+"__________________")
			res = executeSql(getSqlStatement(test + a))
			for c in res:
				result_test.append(str(c))
		except:
			result_test.append("error in sql statement.")
	easy = open("trace.html", "w")
	easy.writelines(gen_diff(result_ref, result_test))

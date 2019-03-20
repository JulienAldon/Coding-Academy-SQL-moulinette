# CODING MOULINETTE SQL

Python Moulinette: SQL Days 1 and 2 in coding_academy

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
1. Clone the repository
2. Create Python environment with venv (or any tool you like)
3. Install dependencies using req.txt (``pip install -r req.txt``)
4. Activate the environment (using venv for example: ``python -m venv <nom de l'env>``)
5. You can now execute the script using ``python3 sqlmouli.py``

or 

2. `chmod +x sqlmouli.py` and execute `./sqlmouli.py <reference_folder> <tested_folder>`

## Usage

`./sqlmouli.py <reference_folder> <tested_folder>`

### Prerequisites

This script will use SqlAlchemy and pymysql

MySQL must be installed and configured, you need to add the sql database, `coding.sql` to your mysql databases

`mysql -u <username> -p < coding.sql` if tested on localhost

This script works with python3 you can download it and install it. 
```
https://www.python.org/downloads/
```
This script use os, sys, difflib and subprocess python modules


## Authors

* **Julien Aldon** - *Initial work* - [Julien Aldon](https://github.com/JulienAldon) for coding-academy.


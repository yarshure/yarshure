#!C:\Python25\python.exe

#EDIT HERE########################################

HOST="localhost"
USER="sa"
PASSWORD="sa"
DATABASE="master"

#DO NOT EDIT BELOW THIS LINE######################

import _mssql
import unittest,types,datetime
try:
    from decimal import Decimal
except ImportError:
    print "Sorry you need at least python 2.4"
    import sys
    sys.exit(1)



    
def setUp():
        self.mssql=_mssql.connect(HOST,USER,PASSWORD)
        self.mssql.select_db(DATABASE)
        self.tableCreated = False
def tearDown():
        if self.tableCreated:
            self.dropTestTable()
        self.mssql.close()
if __name__ == '__main__':
    
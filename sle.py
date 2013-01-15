import sys,time
from socket import *
import _mssql
def sql_login(sql_host,sql_user,sql_pass,sql_dbname):
    con = _mssql.connect(sql_host,sql_user,sql_pass)
    con.select_db(sql_dbname)
    return con
def online_user(sql_handle,sql):
    sql_handle.query(sql)
    row=sql_handle.fetch_array()
    return row
if __name__ == "__main__":
    my_handle = sql_login('localhost','sa','sa','master')
    print time.strftime('%Y-%m-%d %H:%M:%S')
    #my_row=online_user(my_handle,'insert into [master].[dbo].[count1] (timetime,channel_total) values(convert(datetime,str),'num ')
    #print str(my_row[0][2][0][0])
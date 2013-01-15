#!C:\Python25\python.exe
#coding=utf-8

import sys,time
from socket import *
import _mssql
#import socket
#socket.setdefaulttimeout(3.0)

server = [
    'mem_mdc|10.18.88.201:9653',
    'game01_01|10.60.0.11:27011' ,
    'game01_02|10.60.0.11:27012' ,
    'game01_03|10.60.0.11:27013' ,
    'game01_04|10.60.0.11:27015' ,
    'game01_05|10.60.0.11:27016' ,
    'game01_06|10.60.0.11:27017' ,
    'game02_01|10.60.0.12:27011' ,
    'game02_02|10.60.0.13:27012' ,
    'game02_03|10.60.0.12:27013' ,
    'game02_04|10.60.0.12:27015' ,
    'game02_05|10.60.0.12:27016' ,
    'game02_06|10.60.0.12:27017' ,
    'game03_01|10.60.0.13:27011' ,
    'game03_02|10.60.0.13:27012' ,
    'game03_03|10.60.0.13:27013' ,
    'game03_04|10.60.0.13:27015' ,
    'game03_05|10.60.0.13:27016' ,
    'game03_06|10.60.0.13:27017' ,
    
]


def my_socket(serverHost,serverPort):
    try:
        sockobj=socket(AF_INET, SOCK_STREAM)
        sockobj.connect((serverHost, serverPort))
        return 0
        sockobj.close( )
    except error, msg:
        sockobj.close()
        return 1
def sql_login(sql_host,sql_user,sql_pass,sql_dbname):
    con = _mssql.connect(sql_host,sql_user,sql_pass)
    con.select_db(sql_dbname)
    return con

def online_user(sql_handle,sql):
    sql_handle.query(sql)
    row=sql_handle.fetch_array()
    return row
def update_db(sql_handle,sql):
    sql_handle.query(sql)
    row=sql_handle.fetch_array()
    print row
if __name__ == "__main__":
    print "Content-type:text/html"
    print 
    print """<html><head>
            <meta http-equiv="refresh" content="60"; charset="UTF-8">
            </head>
            <font size=1><b>From:IDC  Update : """
    print time.strftime('%Y-%m-%d %H:%M:%S')
    print """</br>Design by: kongxiangbo@higame.com.cn </b></font></br>
    <body>"""
    my_handle = sql_login('10.60.0.230','walter','op5ku20w34','GP_CN')
    my_handle2 = sql_login('localhost','sa','sa','master')
    my_row=online_user(my_handle,'SELECT sum([I_CONNECT]),getdate() FROM [GP_CN].[dbo].[LOGING_CHANNEL]')
    print '在线人数:'+ str(my_row[0][2][0][0])+'    ' +str(my_row[0][2][0][1])+"</br>"
    #outfile="C:\\num.csv"
    #fp1=open(outfile,'a')
    #fp1.write(str(my_row[0][2][0][0])+',' +str(my_row[0][2][0][1])+"\n")
    my_sql="insert into [master].[dbo].[count1] (timetime,channel_total) values(convert(datetime,'"+time.strftime('%Y-%m-%d %H:%M:%S')+"'),"+ str(my_row[0][2][0][0])+')'
    print my_sql
    update_db(my_handle2,my_sql)
    #fp1.close()
    my_handle.close()
    my_handle2.close()
    
    for num in range(0,len(server)):
        if '|' in server[num]:
            name,host=server[num].split('|',1)
            host_ip,host_port=host.split(':',1)
            if my_socket(host_ip,int(host_port))==0 :
                print name+' connect is <font color=green>OK</font></br>'
            else:
                print name+' connect is <font color=red>ERR</font></br>'

    print "</body></html>"            
            
            

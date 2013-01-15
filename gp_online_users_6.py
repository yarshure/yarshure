#!C:\Python25\python.exe
#coding=utf-8
import os,sys
#import _mssql
from socket import *  
import time
import cgi
import cgitb; cgitb.enable()
os.environ[ 'HOME' ] = "C:\\Program Files\\Apache Software Foundation\\Apache2.2\\Apache2\\htdocs\\img\\"
#from pylab import figure, show, nx,xlabel,ylabel,title,savefig
#from matplotlib.dates import DayLocator, HourLocator,MinuteLocator, DateFormatter, drange 
#import matplotlib
import datetime
from gp_ol_plot3 import query,my_plot,my_plot_hour
def getque():
    serverHost = '10.18.88.220'          
    serverPort = 9521                
    sockobj = socket(AF_INET, SOCK_STREAM)      
    sockobj.connect((serverHost, serverPort))   
    data = sockobj.recv(1024)               
#    print 'IPASS Queue:', repr(data)    
    sockobj.close( )        
#    if '), (' in data[2:-2]:
#        site1,site2,site3,site4=data[2:-2].split('), (', 3)
#        print site1,site2,site3,site4
    result=str(data[1:-1])
#    print "debug",data,"||||"
    sites,aa=data.split("||",1)
#    print sites,aa
    d1={"100001":"华东一区:","100002":"华北一区:","100003":"西南天府:","100004":"西安电信:","100005":"华南一区:","100099":"体验区:"}
    d2={"华东一区:":0,"华北一区:":0,"西南天府:":0,"西安电信:":0,"华南一区:":0,"体验区:":0}
    for i in range(0,int(sites)):
        site1,siteO=aa.split("|",1)
        siteID,siteQUE=site1.split(":",1)
        aa=siteO
#        print d1[siteID],siteQUE
#        print d2[d1[siteID]]
        d2[d1[siteID]]=int(siteQUE)
  
#    print d2


    return d2     

if __name__ == "__main__":
    print ("Content-Type: text/html;\n\n")
    print """<html><head><meta http-equiv="refresh" content="60"; charset="UTF-8"></head><body><table><tr><table><tr><td>"""+time.strftime('%Y/%m/%d %H:%M:%S')
    path="C:\\Program Files\\Apache Software Foundation\\Apache2.2\\htdocs\\img\\" 
    file_name='higame_hour1.png'
    online= query()
    print "</td><td>今日最高:"+str(max(online))+"</td><td>今日平均:"+ str(sum(online)/len(online))+"</td><td>今日最低:"+str(min(online))+"</td><td>当前在线:"+str((online[-3]))+"</td>"
    
    print "</table><tr><table><td><font color=blue>Total</font><font color=green>  华东一区</font><font color=red>  华北一区</font><font color=Aqua >  西南天府</font><font color=Fuchsia >  西安电信</font><font color=red ><font color=#FDD017 >  华南一区</font><font color=red ></br>"
    print "IPASS Queue:</br>  "
    d3=getque()
    for key in d3.keys():
        print "%s %s</br>" %(key,d3[key])
    print "</font></td><tr><td>"
    
    
    print "<img src=/img/"+file_name +" width=700 height=700></td><td>"
    
    file_name2='higame.png'    

                
    print "<img src=/img/"+file_name2 +" width=700 height=700></td>"
        
    print "</table></table></body></html>" 








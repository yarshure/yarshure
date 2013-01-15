#!C:\Python25\python.exe
import os,sys
import time
import cgi
import cgitb; cgitb.enable()

# set HOME environment variable to a directory the httpd server can write to
os.environ[ 'HOME' ] = "C:\\Program Files\\Apache Group\\Apache2\\htdocs\\img\\"
print os.environ[ 'HOME' ]

import matplotlib
# chose a non-GUI backend
matplotlib.use( 'Agg' )
#import pylab
from pylab import *
#Deals with inputing data into python from the html form
fp1=open("g:\\gp_csv\\"+time.strftime('%Y%m%d%')+".csv","r")
data=fp1.readlines()
fp1.close()
my_lists=[0]
my_time2=[0]
for num in range(0,len(data)):
    users,my_time=data[num].split(',',1)
    my_time2.append(num)
    my_lists.append(int(users))

# construct your plot
plot(my_time2, my_lists, linewidth=1.0)
xlabel('time (min)')
ylabel('online users ')
title('sun-shine gp online users')
grid(True)
print ("Content-Type: text/html;\n\n")
#pylab.savefig( sys.stdout, format='png' )
file_name=time.strftime('%Y%m%d%H%M%S')+'.png'
dis_dir="C:\\Program Files\\Apache Group\\Apache2\\htdocs\\img\\"
savefig(dis_dir+file_name, format='png' )
#import shutil
#shutil.copyfileobj(open("C:\\Program Files\\Apache Group\\Apache2\\htdocs\\img\\tempfile.png",'rb'), sys.stdout)
print "<html><head></head><body><img src=http://192.168.0.75/img/"+file_name +"></body></html>"
fp1.close()

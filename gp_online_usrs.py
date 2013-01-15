#!C:\Python25\python.exe
from pylab import *

#t = arange(0.0, 2.0, 0.01)
#s = sin(2*pi*t)
def online_users(datafile):
    fp1=open(datafile,"r")
    data=fp1.readlines()
    
    my_lists=[0]
    my_time2=[0]
    for num in range(0,len(data)):
        users,my_time=data[num].split(',',1)
        my_time2.append(num)
        my_lists.append(int(users))
        
    plot(my_time2, my_lists, linewidth=1.0)

    xlabel('time (min)')
    ylabel('online users ')
    title('sun-shine gp online users')
    grid(True)
    savefig('C:\Program Files\Apache Group\Apache2\htdocs\img\gp.png', dpi = 75)
    fp1.close()
 #   show()
     

if __name__ == '__main__':
    online_users("c:\\test4.csv")
    print "Content-type:text/html"
    print 
    print """<html><head>
            <meta http-equiv="refresh" content="60"; charset="UTF-8">
            </head><body>
            <font size=1><b>From:IDC  Update : """
    print time.strftime('%Y-%m-%d %H:%M:%S')
    print """</br>Design by: kongxiangbo@higame.com.cn </b></font></br>"""
    print "<a href=img/gp.png><img src=img/gp.png></a></body></html>"
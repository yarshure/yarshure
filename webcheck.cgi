#!C:\Python25\python.exe

import time
import os
import sys
#sys.stderr = sys.stdout
import httplib
from cgi import escape
import httpExists 
from portal_check import serverurl
from mailExists import smtplogin,pop3login 

#httplib.HTTPConnection.debuglevel = 1
svr_address='61.152.246.77'
mail_user='kongxiangbo@higame.com.cn'
mail_pass='freebsd'

print "Content-type: text/html"
print 
print """<html>
<head>
<title>Networks Portal Site Situation snapshot</title>
<script language="javascript">
function doBlink(){
    var blink = document.all.tags("BLINK")
        for (var i=0; i<blink.length; i++)
            blink[i].style.visibility = blink[i].style.visibility == "" ? "hidden":""
}
    function startBlink() {
        if(document.all)
            setInterval("doBlink()",450)
    }
window.onload = startBlink;
</script>
<meta http-equiv="refresh" content="60">
</head>"""

print """
<body>
<font size=1><b>From:IDC  Update : """
print time.strftime('%Y-%m-%d %H:%M:%S')
print """</br>Design by: kongxiangbo@higame.com.cn </b></font>
<table  width=100%  >
<tr><td>
<table align=right cellspacing=2 cellpadding=2 width=50% border=1 style=border-collapse:collapse;>
<tr>
<th align=center width=25% style=padding-left:10px; padding-right:5px;>
<p align=center><font size=5><B>NAME</B></font></p>
</th>
<td align=center width=25% style=padding-left:10px; padding-right:5px;>
<p align=center><font size=5><B>IP</B></font></p>
</th>
<td align=center width=25% style=padding-left:10px; padding-right:5px;>
<p align=center><font size=5><B>STATUS</B></font></p>
</th>
"""

for num in range(0,(len(serverurl)/2)+1) :
    if '|' in serverurl[num]:
        host_name, url,host_ip = serverurl[num].split('|', 2)
        host,port = host_ip.split(':',1)
        print """<tr>
         <td align=left width=25% style=padding-left:10px; padding-right:5px;><p align=left><font align=left size=5>"""
        print "<a href="+ url +">" + host_name+"</a></font></p></td>"
        print """<td bgcolor=CDCFC4  align=left width=25% style=padding-left:10px; padding-right:5px;>
         <p align=left><font align=left size=5>"""
        print  host_ip+ "</font></p></td>"
        status = httpExists.httpExists(host_ip,url)
        if status ==200 :
            print "<td bgcolor=00FF00   align=center width=25% style=padding-left:10px; padding-right:5px;><p align=center><font size=5>" +str(status) + " OK </font></td>" 
        elif status ==302 and (int(port) ==443 or url=="http://launcher.segame.com/login/login.sega"):
            print "<td bgcolor=00FF00   align=center width=25% style=padding-left:10px; padding-right:5px;><p align=center><font size=5>" +str(status) + " OK </font></td>" 
        else :    
            print "<td bgcolor=red align=center width=25% style=padding-left:10px; padding-right:5px;><p align=center><font color=white size=5><b><blink>"+ str(status) + " ERR</blink> </b></font></p></td>"

print "</table>"

print """<td><table align=left cellspacing=2 cellpadding=2 width=50% border=1 style=border-collapse:collapse;>
<tr>
<th align=center width=25% style=padding-left:10px; padding-right:5px;>
<p align=center><font size=5><B>NAME</B></font></p>
</th>
<th align=center width=25% style=padding-left:10px; padding-right:5px;>
<p align=center><font size=5><B>IP</B></font></p>
</th>
<th align=center width=25% style=padding-left:10px; padding-right:5px;>
<p align=left><font size=5><B>STATUS</B></font></p>
</th>"""

for num in range(len(serverurl)/2+1,len(serverurl)) :
    if '|' in serverurl[num]:
        host_name, url,host_ip = serverurl[num].split('|', 2)
        host,port = host_ip.split(':',1)
        print """
         <tr>
         <td align=left width=25% style=padding-left:10px; padding-right:5px;><p align=left><font align=left size=5>"""
        print "<a href="+ url +">" + host_name+"</a></font></p></td>"
        print """<td bgcolor=CDCFC4  align=left width=25% style=padding-left:10px; padding-right:5px;>
         <p align=left><font align=left size=5>"""
        print  host_ip+ "</font></p></td>"
        status = httpExists.httpExists(host_ip,url)
        if status ==200 :
            print "<td bgcolor=00FF00   align=left width=25% style=padding-left:10px; padding-right:5px;><font size=5><p align=left><font align=left size=5>" +str(status) + " OK</font></p></td>" 
        elif status ==302 and (int(port) ==443 or url=="http://launcher.segame.com/login/login.sega"):
            print "<td bgcolor=00FF00   align=center width=25% style=padding-left:10px; padding-right:5px;><p align=left><font size=5>" +str(status) + " OK </font></p></td>" 
        else :    
            print "<td bgcolor=red align=center width=25% style=padding-left:10px; padding-right:5px;><p align=left><font color=white size=5><b><blink>"+ str(status) + " ERR</blink> </b></font></p></td>"

print """
       <tr>
       <td align=left width=25% style=padding-left:10px; padding-right:5px;><p align=left><font align=left size=5>"""
print "<a href="+ mail_user +">smtp</a></font></p></td>"
print """<td bgcolor=CDCFC4  align=left width=25% style=padding-left:10px; padding-right:5px;>
         <p align=left><font align=left size=5>"""
print  svr_address+ ":25</font></p></td>"
status=smtplogin(svr_address,mail_user,mail_pass)
print "<td bgcolor=00FF00   align=left width=25% style=padding-left:10px; padding-right:5px;><font size=5><p align=left><font align=left size=5>" +str(status) + " OK</font></p></td>" 

print """
       <tr>
       <td align=left width=25% style=padding-left:10px; padding-right:5px;><p align=left><font align=left size=5>"""
print "<a href="+ mail_user +">pop3</a></font></p></td>"
print """<td bgcolor=CDCFC4  align=left width=25% style=padding-left:10px; padding-right:5px;>
         <p align=left><font align=left size=5>"""
print  svr_address+ ":110</font></p></td>"
statuspop3=pop3login(svr_address,mail_user,mail_pass)
print "<td bgcolor=00FF00   align=left width=25% style=padding-left:10px; padding-right:5px;><font size=5><p align=left><font align=left size=5>" +str(statuspop3) + "litter</font></p></td>" 



print "</table>"
print "</table></body></html>"

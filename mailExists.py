from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.Header import Header
from email.Header import decode_header
from types import *
import smtplib,poplib,string,sys,os,email,time
def smtplogin(svr_address,mail_user,mail_pass):
    server=smtplib.SMTP(svr_address)
#server.set_debuglevel(1)           
    server.ehlo()
    server.esmtp_features["auth"] = "LOGIN" 
    code, resp=server.login(mail_user,mail_pass)
    #print code, resp
    server.quit()
    return code
def pop3login(svr_address,mail_user,mail_pass):
    pop=poplib.POP3(svr_address)
#    pop.set_debuglevel(1) 
    pop.user(mail_user)
    pop.pass_(mail_pass)
    count,size = pop.stat( )
    #print count
#print "|||%s||,%d message||" % stat
    pop.quit( )
    return count
if __name__ == '__main__':
    smtp_server=smtplogin()
    smtp_server.quit()
    pop3login()
    

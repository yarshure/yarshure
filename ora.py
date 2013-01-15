#!C:\Python25\python.exe
#coding=utf-8

import cx_Oracle

def db_login(my_tns):
    conn= cx_Oracle.connect(my_tns)
    curs=conn.cursor()
    return curs
def sel_data(curs,sql):
    rr=curs.execute(sql)
    row=curs.fetchone()
    return row
config=[
        "新注册|select count(*) from memb_info_1 where to_date(register_ts)=to_date(sysdate-1)",
        "新激活|select count(*) from memb_active_game_sn where to_date(active_date)=to_date(sysdate-1)",
        "内测号发放帐号|select count(*) from memb_gp_sitesn where status=2 and seq_id>=1  and seq_id <=9730",
        "砸到金蛋的数量|select count(*) from SEED_GP_GETSNBYEGG where to_date(get_time)=to_date(sysdate-1)",
        "砸到金蛋激活的数目|select count(*) from memb_gp_sitesn where seq_id>=40001 and seq_id<=51520 and sn in (select sn from memb_active_game_sn where to_date(active_date)=to_date(sysdate-1))",
]
if __name__ == "__main__":
    print "Content-type:text/html"
    print 
    print "<html><body>"
    my_curs=db_login('ipass/op5ku20w34@ipass')
    
    for num in range(0,len(config)):
        if '|' in config[num]:
            name,my_sql=config[num].split('|',1)
            print name+":     "+str(sel_data(my_curs,my_sql)[0]) +"</br>"
    my_curs.close()
    print "</body></html>"

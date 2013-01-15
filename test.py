import time
file="g:\\gp_csv\\20070607test1.csv"
def my_write(users)
    outfile="g:\\gp_csv\\"+time.strftime('%Y%m%d') + "test.csv"
    fp1=open(outfile,'r')
    data=fp1.readlines()
    num,last=data[len(data)-1].split(',',1)
    fp1.close()
    now=time.strftime('%Y-%m-%d %H:%M')
    if strcmp(now,last):
        print "sjdlkjsdklfjksldjfklsdjklf"
    else:
        fp1=open(outfile,'a+')
        fp1.write(users+time.strftime('%Y-%m-%d %H:%M')+"\n")
        fp1.close()
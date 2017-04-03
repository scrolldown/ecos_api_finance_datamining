import csv
import time
with open('out.csv','wb') as form_f:
    form = csv.writer(form_f,delimiter=',')
    form.writerow(['Count'])
    form.writerow(['STAT_CODE'])
    form.writerow(['ITEM_CODE'])
    form.writerow(['STAT_NAME'])
    form.writerow(['ITEM_NAME1'])
    form.writerow(['UNIT_NAME'])
    form.writerow(['UPDATE_CYCLE'])
    for a in range(19600101,int(time.strftime("%Y%m%d"))):
        y = str(a)[0:4]
        m = str(a)[4:6]
        d = str(a)[6:8]
        if (m == '01' or m == '03' or m=='05' or m=='07' or m=='08' or m=='10' or m=='12'):
            if(int(d) > 0 and int(d) < 32):
                form.writerow([a])
                continue
        elif (m=='04' or m=='06' or m=='09' or m=='11'):
            if(int(d) > 0 and int(d) < 31):
                form.writerow([a])
                continue
        elif (m =='02' and int(y)%4==0):
            if(int(d) > 0 and int(d) < 30):
                form.writerow([a])
                continue
        elif (m=='02' and int(y)%4!=0):
            if(int(d) > 0 and int(d) < 29):
                form.writerow([a])
                continue
        else: continue
        
print 'success'

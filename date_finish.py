# -*- encoding: utf-8 -*-

f=open('date_out.txt','a')
date=('3/20/1')
minvalue=min([int(obj) for obj in date.split('/') if bool(obj)])
amountnumeral=(int(max(date.split('/'), key=lambda i: len(i))))


while True:
    if 2000<=amountnumeral<=2999:
        y=amountnumeral
        year=(str(y))
        f.write(year+'-')
        date=(date.replace(year,''))
        break
    if 00<=minvalue<=99:
        y=(minvalue+2000)
        year=(str(y))
        f.write(year+'-')
        date=(date.replace(str(minvalue),''))
        break
    else:
        print ('is illegal')
        break
minvalue=min([int(obj) for obj in date.split('/') if bool(obj)])
while True:
    if 1<=minvalue<=12:
        month=(str(minvalue))
        f.write('%02d' %minvalue+'-')
        if '%02d' %minvalue in date:
            date=(date.replace('%02d' %minvalue,''))
        else:
            date=(date.replace(str(minvalue),''))
        break
    else:
        print ('is illegal')
        break
if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
    answer='1'
    #print('normal year')
else:
    answer='0'
    #print('leap year')

minvalue=min([int(obj) for obj in date.split('/') if bool(obj)])
daycounter = month
while True:
    if daycounter in ['1', '3', '5', '7', '8', '10', '12']:  
        if 1<=minvalue<=31:
            day=(str(minvalue))
            f.write('%02d' %minvalue+'\n')
            date=(date.replace('%02d' %minvalue,''))
            break
        else:
            print ('is illegal')
            break
    elif daycounter in ['4', '6', '9', '11']:
        if 1<=minvalue<=30:
            day=(str(minvalue))
            f.write('%02d' %minvalue+'\n')
            if '%02d' %minvalue in date:
                date=(date.replace('%02d' %minvalue,''))
            else:
                date=(date.replace(str(minvalue),''))
            break
        if 1<=minvalue>30:
            print ('is illegal')
            break
        else:
            print ('is illegal')
    elif daycounter == '2':    
        if answer == '0':
            if 1<=minvalue<=29:
                day=(str(minvalue))
                f.write('%02d' %minvalue+'\n')
                if '%02d' %minvalue in date:
                    date=(date.replace('%02d' %minvalue,''))
                else:
                    date=(date.replace(str(minvalue),''))
                break
            if 1<=minvalue>29:
                print ('is illegal')
                break
        elif answer == '1':
            if 1<=minvalue<=28:
                day=(str(minvalue))
                f.write('%02d' %minvalue+'\n')
                if '%02d' %minvalue in date:
                    date=(date.replace('%02d' %minvalue,''))
                else:
                    date=(date.replace(str(minvalue),''))            
                break
            if 1<=minvalue>28:
                print ('is illegal')          
                break
    else:
        print('is illegal')
f.close()        
print (minvalue)
print (year+'-'+month+'-'+day)    


    

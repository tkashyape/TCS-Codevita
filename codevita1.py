l=list(input().split(','))
l.sort()
hh=0
mm=0
ss=0
flg=1
if l.count('0')==len(l):
    flg=0
if '1' in l:
    l.remove('1')
    if '2' in l:
        if l.count('0')==4:
            flg=2
           
        elif '1' in l:
            l.remove('1')
            hh='11'
        elif '0' in l:
            l.remove('0')
            hh='10'
        else:
            flg=0
    elif '1' in l:
        l.remove('1')
        hh='11'
    elif '0' in l:
        l.remove('0')
        hh='10'
    else:
        flg=0
elif '0' in l:
    hh='0'+str(max(l))
    l.remove('0')
    l.remove((max(l)))
else:
    flg=0
    
    
if int(max(l))<int(5):
    m=(max(l))
    l.remove(max(l))
    mm=str(m)+str(max(l))
    l.remove(max(l))
elif '5' in l:
    l.remove('5')
    mm='5'+str(max(l))
    l.remove(max(l))
elif '4' in l:
    l.remove('4')
    mm='4'+str(max(l))
    l.remove(max(l))
elif '3' in l:
    l.remove('3')
    mm='3'+str(max(l))
    l.remove(max(l))
elif '2' in l:
    l.remove('2')
    mm='2'+str(max(l))
    l.remove(max(l))
elif '1' in l:
    l.remove('1')
    mm='1'+str(max(l))
    l.remove(max(l))
elif '0' in l:
    l.remove('0')
    mm='0'+str(max(l))
    l.remove(max(l))
else:
    flg=0

    
if int(max(l))<int(5):
    s=(max(l))
    l.remove(max(l))
    ss=str(s)+str(max(l))
elif '5' in l:
    l.remove('5')
    ss='5'+str(max(l))
    l.remove(max(l))
elif '4' in l:
    l.remove('4')
    ss='4'+str(max(l))
    l.remove(max(l))
elif '3' in l:
    l.remove('3')
    ss='3'+str(max(l))
    l.remove(max(l))
elif '2' in l:
    l.remove('2')
    ss='2'+str(max(l))
    l.remove(max(l))
elif '1' in l:
    l.remove('1')
    ss='1'+str(max(l))
    l.remove(max(l))
elif '0' in l:
    l.remove('0')
    ss='0'+str(max(l))
    l.remove(max(l))
else:
    flg=0
if flg==0:
    print('Impossible')
elif flg==2:
    print('12:00:00')
else:
    print(str(hh)+':'+str(mm)+':'+str(ss))

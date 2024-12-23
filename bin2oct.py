def myfind(a,e):
    for i in range(0,len(a)):
        if a[i]==e:
            return i


def bin2oct(b):
    o="";
    convert=['000','001','010','011','100','101','110','111'];
    if(len(b)%3==1):
        b='00'+b;
    else:
        if(len(b)%3==2):
            b='0'+b;
    while(b!=""):
        segment=b[:3];
        o=o+str(myfind(convert,segment))
        b=b[3:]
    return o

print(bin2oct("10110111"))





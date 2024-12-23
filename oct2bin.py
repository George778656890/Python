def myfind(a,e):
    for i in range(0,len(a)):
        if i==e:
            return a[i]






def oct2bin(d):
    convert=['000','001','010','011','100','101','110','111'];
    o="";
    for element in d:
        o=o+myfind(convert,int(element))
    return o

print(oct2bin("111"))
        


        
    

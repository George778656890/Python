def bin2dec(d):
    result=0
    tmp=d[::-1]#reverse the whole sequence to make index match exponent
    for i in range(0,len(tmp)):
        if(tmp[i]=='1'):
            result=result+pow(2,i)#sum of power of index

    return result

print(bin2dec("1111"))
    

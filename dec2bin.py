def dec2bin(num):
    finalresult=''
    if(num==0):
        return 0
    while(num!=0):
        finalresult=str(num%2)+finalresult  #casting remainder into string and concatenation
        num=num//2  #get the quotient to continue modulo
    return finalresult

print(dec2bin(9))

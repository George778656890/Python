alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
cipherKey=[[6,24,1],[13,16,10],[20,17,15]]
deCipherKey=[[8,5,10],[21,8,21],[21,12,8]]

def numToString(num):
    for a in alphabet:
        if(num==(ord(a)-65)):#search by difference of ASCII value
            return a

def stringToNum(string):
    for b in alphabet:
        if(b==string):
            return (ord(string)-65)

def matrix_multiplication(m1,m2):
    if(len(m1[0])!=len(m2)):
        print("The sizes of two matrice don't match,can't perform multiplication")
        
    else:
        final_matrix=[0]*len(m1)
        for d in range(0,len(m1)):
            final_matrix[d]=[0]*len(m2[0])#construct a new matrix based on two original matrices

        for i in range(0,len(m1)):
            for j in range(0,len(m2[0])):
                total=0
                for k in range(0,len(m1[0])):
                    total=total+m1[i][k]*m2[k][j]
                final_matrix[i][j]=total
    return final_matrix


def cipher(cipherKeyMatrix,plainText):
    plainTextMatrix=[0]*3
    for e in range(0,len(plainTextMatrix)):
        plainTextMatrix[e]=[0]*(len(plainText)//3)#construct matrix for plainText message

    counter=0#convert plaintText into number,and store in plainTextMatrix
    for column in range(0,len(plainTextMatrix[0])):#Column control
        for row in range(0,len(plainTextMatrix)):  #Row control
            plainTextMatrix[row][column]=stringToNum(plainText[counter])
            counter=counter+1

    tmp=matrix_multiplication(cipherKeyMatrix,plainTextMatrix)

    for i in range(0,len(tmp)):#Row control
        for j in range(0,len(tmp[0])):#Column control
            tmp[i][j]=tmp[i][j]%26

    cipherText=''
    for column in range(0,len(tmp[0])):#Column control
        for row in range(0,len(tmp)):  #Row control
            cipherText=cipherText+numToString(tmp[row][column])

    return cipherText


    
def decipher(deCipherKeyMatrix,cipherText):
    cipherTextMatrix=[0]*3
    for e in range(0,len(cipherTextMatrix)):
        cipherTextMatrix[e]=[0]*(len(cipherText)//3)#construct matrix for cipherText message

    counter=0#convert cipherText into number,and store in cipherTextMatrix
    for column in range(0,len(cipherTextMatrix[0])):#Column control
        for row in range(0,len(cipherTextMatrix)):  #Row control
            cipherTextMatrix[row][column]=stringToNum(cipherText[counter])
            counter=counter+1
            
    tmp=matrix_multiplication(deCipherKeyMatrix,cipherTextMatrix)

    for i in range(0,len(tmp)):#Row control
        for j in range(0,len(tmp[0])):#Column control
            tmp[i][j]=tmp[i][j]%26

    plainText=''
    for column in range(0,len(tmp[0])):#Column control
        for row in range(0,len(tmp)):  #Row control
            plainText=plainText+numToString(tmp[row][column])

    return plainText

print(cipher(cipherKey,'SELLITNOW'))
print(decipher(deCipherKey,'HSVRTRUPW'))

























                





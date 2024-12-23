def matBuild(n,m):
    A=[0]*n
    for i in range(n):
        A[i]=[0]*m
    return A


def matPrint(A):
    print('-'*10)
    for i in A:
        for j in i:
            print(j,end=' ')
        print()
    print('-'*10)


def matMultBool(A,B,C):
    if(len(A[0])!=len(B)):
        print("The sizes of two matrice don't match,can't perform multiplication")
        
    else:
        for i in range(0,len(A)):
            for j in range(0,len(B[0])):
                total=0
                for k in range(0,len(A[0])):
                    total=total or A[i][k] and B[k][j]
                C[i][j]=total
    return 


def matAddBool(A,B):
    C=matBuild(5,5)
    for i in range(0,len(A)):#Row control
        for j in range(0,len(A[0])):#Column control
            C[i][j]=A[i][j] or B[i][j]
    return C


def buildAdj(r,R):
    for i in r:
        R[i[0]][i[1]]=1
    return


def buildSmallr(R):
    relationList=[]
    for i in range(0,len(R)):
        for j in range(0,len(R[0])):
            if(R[i][j]==1):
                relationList=relationList+[(i,j)]
    return relationList
    


def myMain():
#We assume that the set A = {0,1,2,3,4}
    r=[(1,1),(2,2),(3,3),(1,2),(2,3),(4,4)]
    R=matBuild(5,5)
    buildAdj(r,R)
    matPrint(R)
    R2=matBuild(5,5)
    matMultBool(R,R,R2)
    matPrint(R2)
    R3=matBuild(5,5)
    matMultBool(R,R2,R3)
    matPrint(R3)
    R4=matBuild(5,5)
    matMultBool(R,R3,R4)
    matPrint(R4)
    R5=matBuild(5,5)
    matMultBool(R,R4,R5)
    matPrint(R5)
    R_final=matBuild(5,5)
    R_final=matAddBool(matAddBool(matAddBool(matAddBool(R,R2),R3),R4),R5)
    r2=buildSmallr(R_final)
    print(r2)

print("starting...")
myMain()




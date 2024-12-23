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
                    total=total or m1[i][k] and m2[k][j]
                final_matrix[i][j]=total
    return final_matrix


a1=[[1,1,0],[0,0,1],[0,0,1]]
a2=[[1,1,0],[0,0,1],[0,0,1]]

print(matrix_multiplication(a1,a2))

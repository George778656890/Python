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


a1=[[6,24,1],[13,16,10],[20,17,15]]
a2=[[18,11,13],[4,8,14],[11,19,22]]

print(matrix_multiplication(a1,a2))

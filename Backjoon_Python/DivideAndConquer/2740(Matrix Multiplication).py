#2740 행렬 곱셈
matrixA=[]
matrixB=[]
N,M=input().split()
N=int(N)
M=int(M)
for i in range(N):
    temp=map(int,input().split())
    matrixA.append(list(temp))

N,M=input().split()
N=int(N)
M=int(M)
for i in range(N):
    temp=map(int,input().split())
    matrixB.append(list(temp))

#for i in range(len(matrixA)):
#    for j in range(len(matrixB)):
#        print(matrixA[i][j]*matrixB[j][i],end=" ")
#    print()


    #1  2        -1  -2  0
    #3  4         0   0  3
    #5  6
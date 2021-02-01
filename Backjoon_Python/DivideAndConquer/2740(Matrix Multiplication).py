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

for i in range(len(matrixA)):
    for j in range(len(matrixB[0])):
        num=0
        for k in range(len(matrixB)):
            num+=matrixA[i][k]*matrixB[k][j]
        print(num,end=" ")
    print()

#1080 행렬
n,m=map(int,input().split())
matrix_a=[]
matrix_b=[]
res=0

def change_matrix(array,a,b):
    for i in range(a,a+3):
        for j in range(b,b+3):
            array[i][j]=(array[i][j]+1)%2

for i in range(n):
    temp=list(map(int,input()))
    matrix_a.append(temp)
for i in range(n):
    temp=list(map(int,input()))
    matrix_b.append(temp)

for i in range(n-2):
    for j in range(m-2):
        if matrix_a[i][j]!=matrix_b[i][j]:
            change_matrix(matrix_a,i,j)
            res+=1

if matrix_a==matrix_b:
    print(res)
else:
    print(-1)
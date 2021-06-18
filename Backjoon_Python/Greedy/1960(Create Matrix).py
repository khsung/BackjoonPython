#1960 행렬 만들기
n=int(input())
matrix=[[0 for i in range(n)]for j in range(n)]
row=list(map(int,input().split()))
col=list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if col[j]>0 and row[i]>0:
            matrix[i][j]=1
            col[j]-=1
            row[i]-=1

if row.count(0)==n and col.count(0)==n:
    print(1)
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=" ")
        print()
else:
    print(-1)
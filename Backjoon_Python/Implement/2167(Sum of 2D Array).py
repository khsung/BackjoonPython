#2167 2차원 배열의 합
N,M=map(int,input().split())
array=[]
sum_array=[]
for i in range(N):
    temp=list(map(int,input().split()))
    array.append(temp)
for i in range(N):
    sum_array.append([])
    sum_val=0
    for j in range(M):
        sum_val+=array[i][j]
        sum_array[i].append(sum_val)

K=int(input())
for i in range(K):
    a,b,x,y=map(int,input().split())
    a-=1
    b-=1
    x-=1
    y-=1
    res=0
    if b==0:
        for j in range(a,x+1):
            res+=sum_array[j][y]
    else:
        for j in range(a,x+1):
            res=res+sum_array[j][y]-sum_array[j][b-1]
    print(res)
#16926 배열 돌리기 1 구현 중
N,M,R=map(int,input().split())
R=R%(2*(N+M-2))
array=[]
res_array=[[0 for i in range(M)]for i in range(N)]
for i in range(N):
    temp=list(input().split())
    array.append(temp)

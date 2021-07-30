#12865 평범한 배낭
n,k=map(int,input().split())
res=0
#n개, 무게, 가치
dp=[[0,0,0] for i in range(k+1)]
p_info=[]
for i in range(n):
    p_info.append(list(map(int,input().split())))

visited=[0 for i in range(n)]

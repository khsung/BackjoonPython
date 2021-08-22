#20055 컨베이어 벨트 위의 로봇
from collections import deque
n,k=map(int,input().split())
cnt_zero=0
res=0
temp_belt=list(map(int,input().split()))
belt=deque()
for i in temp_belt:
                #내구도, 로봇
    belt.append([i,0])
while True:
    res+=1
    temp=belt.pop()
    if temp[1]!=0:
        temp[1]=0
    belt.appendleft(temp)
    belt[n-1][1]=0
    for i in range(n-2,-1,-1):
        if belt[i][1]!=0 and belt[i+1][1]==0 and belt[i+1][0]>0:
            belt[i][1],belt[i+1][1]=belt[i+1][1],belt[i][1]
            belt[i+1][0]-=1
            if belt[i+1][0]==0:
                cnt_zero+=1

    if belt[0][0]!=0:
        belt[0][0]-=1
        belt[0][1]=1
        if belt[0][0]==0:
            cnt_zero+=1
    if cnt_zero>=k:
        break
print(res)
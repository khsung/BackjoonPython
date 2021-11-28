#B번 - 벼락치기
n=int(input())
chap=[]
for i in range(n):
    chap.append(int(input()))
curr=0
res=0
while curr<len(chap):
    temp_time=30
    while temp_time>0 and curr<len(chap):
        if temp_time<=chap[curr]:
            if chap[curr]<=temp_time*2:
                res+=1
                temp_time=0
            temp_time=0
        else:
            res+=1
            temp_time-=chap[curr]
            curr+=1
    curr+=1
print(res)
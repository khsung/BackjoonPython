#1806 부분합
n,s=map(int,input().split())
sequence=list(map(int,input().split()))
tempsum=0
maxindexsize=100001
start=end=0
plusstart=True
while start<n:
    if plusstart==True:
        tempsum+=sequence[start]
    if tempsum<s:
        start+=1
        plusstart=True
    else:
        if start-end+1<maxindexsize:
            maxindexsize=start-end+1
        tempsum-=sequence[end]
        end+=1
        plusstart=False

if maxindexsize==100001:
    print(0)
else:
    print(maxindexsize)
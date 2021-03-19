#14501 퇴사 미완성
schedule=[]
n=int(input())
maxsum=0
for i in range(n):
    a,b=map(int,input().split())
    schedule.append([a,b])
for i in range(1,n+1):
    tempsum=0
    day=i
    for j in range(i,n+1):
        if schedule[j-1][0]+i-1<n and day<=j and day+schedule[j-1][0]<=n:
            tempsum+=schedule[j-1][1]
            day+=schedule[j-1][0]
            print("j =",j,"day =",day)
    if maxsum<tempsum:
        maxsum=tempsum
    print("tempsum =",tempsum)
print(maxsum)
#14501 퇴사
schedule=[]
n=int(input())
maxsum=0
for i in range(n):
    a,b=map(int,input().split())
    schedule.append([a,b])
for i in range(n):
    tempsum=0
    day=i-1
    currdate=i
    for j in range(i,n):
        if day+schedule[j][0]<n and day<j:
            day=day+schedule[j][0]
            tempsum+=schedule[j][1]
    if maxsum<tempsum:
        maxsum=tempsum
print(maxsum)
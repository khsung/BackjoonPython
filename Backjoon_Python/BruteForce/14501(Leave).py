#14501 퇴사 미완성
schedule=[]
n=int(input())
maxsum=0
for i in range(n):
    a,b=map(int,input().split())
    schedule.append([a,b])
for i in range(n):
    tempsum=0
    day=i
    for j in range(i,n):
        if day+schedule[j][0]-1<n-1 and day<=j:
            day=day+schedule[j][0]
            tempsum+=schedule[j][1]
            print(j,day,schedule[j][0],schedule[j][1])
    if maxsum<tempsum:
        maxsum=tempsum
    print("tempsum =",tempsum)
print(maxsum)
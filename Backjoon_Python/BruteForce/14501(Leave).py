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
        if schedule[i][0]+i<=n and day<=j:
            tempsum+=schedule[i][1]
            day+=schedule[i][0]
            print("j =",j,"day =",day)
    if maxsum<tempsum:
        maxsum=tempsum
    print("i =",i)
print(maxsum)
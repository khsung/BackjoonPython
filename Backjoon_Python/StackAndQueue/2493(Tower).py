#2493 탑 시간초과 
n=int(input())
towers=list(map(int,input().split()))
res=[0 for i in range(n)]
for i in range(len(towers)-1,0,-1):
    for j in range(i-1,0,-1):
        if towers[j]>towers[i]:
            res[i]=towers[j]
            break
print(res)
#17224 APC는 왜 서브태스크 대회가 되었을까?
n,l,k=map(int,input().split())
problem=[]
for i in range(n):
    temp=list(map(int,input().split()))
    problem.append(temp)
problem=sorted(problem, key=lambda x:(x[1],x[0]),reverse=True)
cnt=0
res=0
save_problem=[]
for i in range(len(problem)):
    if problem[i][1]<=l and cnt<k:
        cnt+=1
        res+=140
        save_problem.append(problem[i])
for i in range(len(problem)):
    if problem[i][0]<=l and cnt<k and problem[i] not in save_problem:
        cnt+=1
        res+=100
print(res)
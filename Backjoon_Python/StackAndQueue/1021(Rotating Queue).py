#1021 회전하는 큐
n,m=map(int, input().split())
queuem=list(map(int,input().split()))
queuen=[i+1 for i in range(n)]
res=0
while len(queuem)>0:
    if queuem[0]==queuen[0]:
        queuem.pop(0)
        queuen.pop(0)
    else:
        if queuen.index(queuem[0])<=len(queuen)//2:
            while queuen[0]!=queuem[0]:
                queuen.append(queuen.pop(0))
                res+=1
        else:
            while queuen[0]!=queuem[0]:
                queuen.insert(0,queuen.pop())
                res+=1
print(res)
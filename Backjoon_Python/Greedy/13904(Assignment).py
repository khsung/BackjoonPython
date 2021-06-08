#13904 과제
n=int(input())
assign=[]
maxday=0
res=0

for i in range(n):
    temp=list(map(int,input().split()))
    if maxday<temp[0]:
        maxday=temp[0]
    assign.append(temp)
assign=sorted(assign,key=lambda x:(-x[0],-x[1]))
day=assign[0][0]
index=0
for i in range(day,0,-1):
    max=0
    temparr=[]
    for j in assign:
        if j[0]>=i:
            if j[1]>max:
                max=j[1]
                temparr=[j[0],j[1]]
    if len(temparr)>0:
        res+=temparr[1]
        assign.remove(temparr)
print(res)
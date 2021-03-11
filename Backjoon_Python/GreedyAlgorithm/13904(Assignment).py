#13904 과제(미완성)
n=int(input())
assign=[]
maxday=0
res=0
cnt=0
for i in range(n):
    temp=list(map(int,input().split()))
    if maxday<temp[0]:
        maxday=temp[0]
    assign.append(temp)
assign=sorted(assign,key=lambda x:(-x[1],x[0]))
for i in range(len(assign)):
    if assign[i][0]>cnt:
        cnt+=1
        res+=assign[i][1]
print(assign)
print(res)
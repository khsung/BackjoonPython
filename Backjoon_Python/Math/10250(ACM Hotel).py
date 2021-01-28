
#10250 ACM 호텔
testcase=int(input())
res=[]

for i in range(testcase):
    h,w,n=input().split(" ")
    if int(n)%int(h)==0:
        x=int(int(n)/int(h))
        y=int(h)
    else:
        x=int(int(n)/int(h))+1
        y=int(n)%int(h)
    res.append(100*y+x)
for i in range(len(res)):
    print(res[i])
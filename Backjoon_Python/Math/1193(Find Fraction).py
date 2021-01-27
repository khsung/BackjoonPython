#1193 분수찾기
num = int(input())
count=0
sum=0
while sum<num:
    count+=1
    sum+=count
if count%2==0:
    up=True
    a=count
    b=1
else:
    up=False
    a=1
    b=count
res=sum-num
if up==True:
    a-=res
    b+=res
else:
    a+=res
    b-=res
print(a,end="")
print("/",end="")
print(b,end="")
#1837 암호제작
p,k=map(int,input().split())
check=False
for i in range(2,k):
    if p%i==0:
        res=i
        check=True
        break
if check:
    print("BAD",res)
else:
    print("GOOD")
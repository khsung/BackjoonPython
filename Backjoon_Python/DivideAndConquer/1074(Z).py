#1074 Z
N,r,c=map(int,input().split())
res=0
r+=1
c+=1
topr=1
bottomr=2**N
leftc=1
rightc=2**N
while bottomr-topr!=0:
    if (bottomr+topr)//2>=r:
        bottomr=(bottomr+topr)//2
        if (rightc+leftc)//2>=c:
            rightc=(rightc+leftc)//2
        else:
            leftc=(rightc+leftc)//2+1
            res=res+(bottomr-topr+1)*(bottomr-topr+1)
    else:
        topr=(bottomr+topr)//2+1
        if (rightc+leftc)//2>=c:
            rightc=(rightc+leftc)//2
            res=res+(bottomr-topr+1)*(bottomr-topr+1)*2
        else:
            leftc=(rightc+leftc)//2+1
            res=res+(bottomr-topr+1)*(bottomr-topr+1)*3
print(res)
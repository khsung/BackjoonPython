#2960 에라토스테네스의 체
n,k=map(int,input().split())
era=[0 for i in range(n+1)]
era[0]=era[1]=1
cnt=0
index=2
while True:
    if era[index]==0:
        era[index]=1
        cnt+=1
        if cnt ==k:
            print(index)
            break
        for i in range(index+1,len(era)):
            if i%index==0 and era[i]==0:
                era[i]=1
                cnt+=1
                if cnt ==k:
                    res=i
                    break
    if cnt==k:
        print(res)
        break
    else:
        index+=1
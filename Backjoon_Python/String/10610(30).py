#10610 30
n=input()
sum=0
cnt=0
array=[]
res=""
if "0" not in n:
    print(-1)
else:
    for i in range(len(n)):
        if n[i]=="0":
            cnt+=1
        else:
            array.append(n[i])
        sum+=int(n[i])
    if sum%3==0:
        array.sort(reverse=True)
        for i in range(len(array)):
            res+=array[i]
        for i in range(cnt):
            res+="0"
        print(int(res))
    else:
        print(-1)
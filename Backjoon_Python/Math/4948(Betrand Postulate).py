#4948 Betrand Postulate
num=1
res=[]
rescount=[]
while True:
    num=int(input())
    if num==0:
        break
    else:
        count=0
        a=num
        b=2*num
        prime=[1 for i in range(b+1)]
        prime[0]=0
        prime[1]=0
        for i in range(2,b+1):
            temp=2*i
            while temp<=b:
                prime[temp]=0
                temp+=i
        for i in range(a,b+1):
            if prime[i]==1:
                res.append(i)


for i in range(len(res)):
    print(rescount[i])



#num=1
#res=[]
#while True:
#    num=int(input())
#    if num==0:
#        break
#    else:
#        count=0
#        a=num
#        b=2*num
#        prime=[1 for i in range(b+1)]
#        prime[0]=0
#        prime[1]=0
#        for i in range(2,b+1):
#            check=0
#            temp=2*i
#            while temp<=b:
#                prime[temp]=0
#                temp+=i
#        for i in range(a+1,b+1):
#            if prime[i]==1:
#                count+=1
#        res.append(count)

#for i in range(len(res)):
#    print(res[i])
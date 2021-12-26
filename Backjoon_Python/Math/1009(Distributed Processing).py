#1009 분산처리
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if a==1:
        print(1)
    else:
        last=a%10
        last_num=[last]
        sum_last=(last**2)%10
        while sum_last not in last_num:
            last_num.append(sum_last)
            sum_last=(sum_last*last)%10
        if last_num[(b-1)%len(last_num)]==0:
            print(10)
        else:
            print(last_num[(b-1)%len(last_num)])


#n=int(input())
#for i in range(n):
#    a,b=map(int,input().split())
#    print(a**b%10)
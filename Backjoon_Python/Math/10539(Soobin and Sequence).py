#10539 수빈이와 수열
n=int(input())
b=list(map(int,input().split()))
cnt=0
temp_sum=0
for i in range(n):
    cnt+=1
    print(b[i]*cnt-temp_sum,end=" ")
    temp_sum=b[i]*cnt
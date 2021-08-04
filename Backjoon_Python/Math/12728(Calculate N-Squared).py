#12728 n제곱 계산
import math
test_case=int(input())
dp=[0 for i in range(32)]
dp[0]=(3+math.sqrt(5))**0
dp[1]=round((3+math.sqrt(5))**1,5)
print(dp[1])
for i in range(2,len(dp)):
    dp[i]=round(dp[i-1]**2,15)%1000
print(dp)
for i in range(1,test_case+1):
    n=int(input())
    temp=int((3+math.sqrt(5))**n)

    temp=str(temp%1000)
    temp=temp.zfill(3)
    print("Case #",i,":",sep="",end="")
    print("",temp)
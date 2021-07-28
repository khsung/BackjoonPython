#1915 가장 큰 정사각형
import sys
n,m=map(int,input().split())
dp=[]
res=1
check=False
for i in range(n):
    temp=list(map(int,list(sys.stdin.readline().rstrip())))
    temp.insert(0,0)
    if 1 in temp:
        check=True
    for j in range(1,m+1):
        temp[j]+=temp[j-1]
    dp.append(temp)

if not check:
    print(0)
else:
    for i in range(n):
        for j in range(1,m+1):
            if dp[i][j]==0:
                continue
            elif dp[i][j]-dp[i][j-1]==0:
                continue
            else:
                width=res+1
                square_check=True
                while square_check:
                    if i+width>n or j+width-1>m:
                        break
                    else:
                        temp_sum=0
                        for k in range(i,i+width):
                            temp_sum+=(dp[k][j+width-1]-dp[k][j-1])
                        if temp_sum==width*width:
                            if width>res:
                                res=width
                            width+=1
                        else:
                            square_check=False
    print(res*res)
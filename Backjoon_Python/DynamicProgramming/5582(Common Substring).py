#5582 공통 부분 문자열
import sys
first=list(sys.stdin.readline().rstrip())
second=list(sys.stdin.readline().rstrip())
res=0
dp=[[0 for i in range(len(first)+1)]for j in range(len(second)+1)]
for i in range(1,len(second)+1):
    for j in range(1,len(first)+1):
        if second[i-1]==first[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
            if res<dp[i][j]:
                res=dp[i][j]
print(res)
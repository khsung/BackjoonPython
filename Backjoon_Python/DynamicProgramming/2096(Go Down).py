#2096 내려가기
import copy,sys
n=int(input())
max_dp=[]
max_dp.append(list(map(int,sys.stdin.readline().split())))
max_dp.append([max_dp[0][0],max_dp[0][1],max_dp[0][2]])
min_dp=copy.deepcopy(max_dp)
for i in range(n-1):
    temp=list(map(int,sys.stdin.readline().split()))
    max_dp[1][0]=max(max_dp[0][0],max_dp[0][1])+temp[0]
    min_dp[1][0]=min(min_dp[0][0],min_dp[0][1])+temp[0]

    max_dp[1][1]=max(max_dp[0][0],max_dp[0][1],max_dp[0][2])+temp[1]
    min_dp[1][1]=min(min_dp[0][0],min_dp[0][1],min_dp[0][2])+temp[1]

    max_dp[1][2]=max(max_dp[0][2],max_dp[0][1])+temp[2]
    min_dp[1][2]=min(min_dp[0][2],min_dp[0][1])+temp[2]

    max_dp[0][0],max_dp[0][1],max_dp[0][2]=max_dp[1][0],max_dp[1][1],max_dp[1][2]
    min_dp[0][0],min_dp[0][1],min_dp[0][2]=min_dp[1][0],min_dp[1][1],min_dp[1][2]

print(max(max_dp[1]),min(min_dp[1]))
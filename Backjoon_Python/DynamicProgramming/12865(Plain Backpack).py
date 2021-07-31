#12865 평범한 배낭
import copy,sys
n,k=map(int,input().split())
res=0
#무게, 가치, visited
dp=[[0,0,[0 for j in range(n)]] for i in range(k+1)]
p_info=[]
for i in range(n):
    p_info.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,k+1):
    for j in range(len(p_info)):
        if i>=p_info[j][0]:
            if dp[i][1]<dp[i-p_info[j][0]][1]+p_info[j][1] and dp[i-p_info[j][0]][2][j]==0:
                dp[i][0]=dp[i-p_info[j][0]][0]+p_info[j][0]
                dp[i][1]=dp[i-p_info[j][0]][1]+p_info[j][1]
                dp[i][2]=copy.deepcopy(dp[i-p_info[j][0]][2])
                dp[i][2][j]=1
                if res<dp[i][1]:
                    res=dp[i][1]
print(res)
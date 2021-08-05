# 1번 가희야 거기서 자는거 아니야
r,c=map(int,input().split())
r_g,c_g,r_p,c_p=map(int,input().split())
cnt_sum=0
for i in range(r):
    temp=list(input())
    cnt_sum+=temp.count("P")
if cnt_sum==r_p*c_p:
    print(0)
else:
    print(1)
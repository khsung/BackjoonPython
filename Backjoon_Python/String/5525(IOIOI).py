#5525 IOIOI
import sys
n=int(input())
m=int(input())
p_list=sys.stdin.readline().rstrip()
curr_index=0
p_cnt=[]
while curr_index<m:
    if p_list[curr_index]=="I":
        cnt=0
        while curr_index+2<m and p_list[curr_index+1:curr_index+3]=="OI":
            curr_index+=2
            cnt+=1
        p_cnt.append(cnt)
    curr_index+=1
res=0
for i in p_cnt:
    if i>=n:
        res+=(i-n+1)
print(res)
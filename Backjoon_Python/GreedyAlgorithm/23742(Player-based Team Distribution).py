#23742 Player-based Team Distribution
n=int(input())
num_list=list(map(int,input().split()))
minus_index=0
plus_sum=0
plus_cnt=0
total_sum=sum(num_list)
num_list.sort(reverse=True)
check=True
res=0
for i in range(len(num_list)):
    if num_list[i]>0:
        plus_sum+=num_list[i]
        plus_cnt+=1
    else:
        minus_index=i
        break

minus_sum=total_sum-plus_sum
res=plus_sum*plus_cnt+minus_sum
for i in range(minus_index,len(num_list)):
    plus_sum+=num_list[i]
    plus_cnt+=1
    minus_sum-=num_list[i]
    if res<plus_sum*plus_cnt+minus_sum:
        res=plus_sum*plus_cnt+minus_sum
print(res)
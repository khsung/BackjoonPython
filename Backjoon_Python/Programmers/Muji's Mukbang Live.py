#무지의 먹방 라이브
def solution(food_times, k):
    answer = 0
    if sum(food_times)<=k:
        return -1
    else:
        sorted_time=sorted(food_times)
        temp_sum=0
        last_value=0
        for i in range(len(sorted_time)):
            temp_sum+=((sorted_time[i]-last_value)*(len(sorted_time)-i))
            if temp_sum>k:
                temp_sum-=((sorted_time[i]-last_value)*(len(sorted_time)-i))
                res=k-temp_sum+1
                temp_cnt=0
                for j in range(len(food_times)):
                    if food_times[j]>=sorted_time[i]:
                        temp_cnt+=1
                        if temp_cnt==res:
                            return j+1

            else:
                last_value=sorted_time[i]

food_times=[3, 1, 2]
k=5

print(solution(food_times, k))
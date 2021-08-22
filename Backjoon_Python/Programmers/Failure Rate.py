#실패율
def solution(N, stages):
    answer = []
    temp_ans=[]
    stages.sort(reverse=True)
    for i in range(1,N+1):
        temp_cnt=0
        curr_size=len(stages)
        while len(stages)>0 and stages[len(stages)-1]==i:
            temp_cnt+=1
            stages.pop()
        if curr_size!=0:
            temp_ans.append([i,temp_cnt/curr_size])
        else:
            temp_ans.append([i,0])
    temp_ans.sort(key=lambda x:-x[1])
    for i in temp_ans:
        answer.append(i[0])
    return answer

N=[2]
stages=[[1,1]]
for i in range(len(N)):
    print(solution(N[i],stages[i]))
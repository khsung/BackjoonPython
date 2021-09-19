#입실 퇴실
def solution(enter, leave):
    answer = [0 for i in range(len(enter))]

    for i in range(len(enter)):
        visited=[0 for a in range(len(enter))]
        for j in range(i+1,len(enter)):
            visited[enter[j]-1]=1
        for j in range(len(leave)):
            if leave[j]==enter[i]:
                break
            elif visited[leave[j]-1]==1:
                answer[enter[i]-1]+=1
                answer[leave[j]-1]+=1

    return answer

enter=[[1,3,2],[1,4,2,3],[3,2,1],[3,2,1],[1,4,2,3]]
leave=[[1,2,3],[2,1,3,4],[2,1,3],[1,3,2],[2,1,4,3]]

for i in range(len(enter)):
    print(solution(enter[i], leave[i]))
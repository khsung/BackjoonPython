#입실 퇴실
def solution(enter, leave):
    answer = []
    visited=[0 for i in range(len(enter))]
    return answer

enter=[[1,3,2],[1,4,2,3],[3,2,1],[3,2,1],[1,4,2,3]]
leave=[[1,2,3],[2,1,3,4],[2,1,3],[1,3,2],[2,1,4,3]]

for i in range(len(enter)):
    print(solution(enter[i], leave[i]))
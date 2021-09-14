#합승 택시 요금
def solution(n, s, a, b, fares):
    INF=float('inf')
    answer = INF
    
        #도착지점, cost
    path=[[]for i in range(n)]
    for i in range(len(fares)):
        path[fares[i][0]-1].append([fares[i][1]-1,fares[i][2]])
        path[fares[i][1]-1].append([fares[i][0]-1,fares[i][2]])
    
    cost_to_mid=[INF for i in range(n)]
    cost_to_mid[s-1]=0
    start=s-1
    visited=[0 for i in range(n)]
    for j in range(n):
            visited[start]=1
            for k in range(len(path[start])):
                if cost_to_mid[path[start][k][0]]>cost_to_mid[start]+path[start][k][1]:
                    cost_to_mid[path[start][k][0]]=cost_to_mid[start]+path[start][k][1]
            temp=INF
            for k in range(n):
                if visited[k]==0 and temp>cost_to_mid[k]:
                    temp=cost_to_mid[k]
                    start=k

    for i in range(n):
        mid=i
        cost_to_end=[INF for i in range(n)]
        cost_to_end[mid]=0
        start=mid
        visited=[0 for i in range(n)]
        for j in range(n):
            visited[start]=1
            for k in range(len(path[start])):
                if cost_to_end[path[start][k][0]]>cost_to_end[start]+path[start][k][1]:
                    cost_to_end[path[start][k][0]]=cost_to_end[start]+path[start][k][1]
            temp=INF
            for k in range(n):
                if visited[k]==0 and temp>cost_to_end[k]:
                    temp=cost_to_end[k]
                    start=k

        if answer>cost_to_mid[mid]+cost_to_end[a-1]+cost_to_end[b-1]:
            answer=cost_to_mid[mid]+cost_to_end[a-1]+cost_to_end[b-1]

    return answer

n=[6,7,6]
s=[4,3,4]
a=[6,4,5]
b=[2,1,6]
fares=[[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]],[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]],[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]]

for i in range(len(n)):
    print(solution(n[i], s[i], a[i], b[i], fares[i]))
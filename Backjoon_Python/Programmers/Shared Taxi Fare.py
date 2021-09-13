#합승 택시 요금
def solution(n, s, a, b, fares):
    answer = 0
    INF=float('inf')
    cost=[INF for i in range(n)]

        #도착지점, cost
    path=[[]for i in range(n)]
    for i in range(len(fares)):
        path[fares[i][0]-1].append([fares[i][1]-1,fares[i][2]])
        path[fares[i][1]-1].append([fares[i][0]-1,fares[i][2]])
    
    for i in range(n):
        mid=i


    return answer

n=[6,7,6]
s=[4,3,4]
a=[6,4,5]
b=[2,1,6]
fares=[[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]],[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]],[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]]

for i in range(len(n)):
    print(solution(n[i], s[i], a[i], b[i], fares[i]))
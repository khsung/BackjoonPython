#복서 정렬하기
def solution(weights, head2head):
    answer = []
    #복서 번호,전체 승률,자신보다 무거운 복서를 이긴 횟수, 자신의 무게
    boxer=[[i+1] for i in range(len(weights))]
    for i in range(len(head2head)):
        try:
            boxer[i].append((head2head[i].count("W")*100)/(len(head2head[i])-head2head[i].count("N")))
        except:
            boxer[i].append(0)
        boxer[i].append(0)
        for j in range(len(head2head[i])):
            if head2head[i][j]=="W":
                if weights[i]<weights[j]:
                    boxer[i][2]+=1
        boxer[i].append(weights[i])
    boxer.sort(key=lambda x:(-x[1],-x[2],-x[3],x[0]))
    for i in range(len(boxer)):
        answer.append(boxer[i][0])
    return answer

weights=[[50,82,75,120],[145,92,86],[60,70,60]]
head2head=[["NLWL","WNLL","LWNW","WWLN"],["NLW","WNL","LWN"],["NNN","NNN","NNN"]]

for i in range(len(weights)):
    print(solution(weights[i], head2head[i]))
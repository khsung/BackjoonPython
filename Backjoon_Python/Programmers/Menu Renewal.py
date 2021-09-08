#메뉴 리뉴얼
from itertools import combinations

def solution(orders, course):
    answer = []
    alpha=[]
    maxlen=0
    for i in range(len(orders)):
        if len(orders[i])>maxlen:
            maxlen=len(orders[i])
        orders[i]="".join(sorted(orders[i]))
        for j in range(len(orders[i])):
            if orders[i][j] not in alpha:
                alpha.append(orders[i][j])
    for i in course:
        if maxlen>=i:
            max_cnt=0
            temp_res=[]
            comb_list=list(combinations(alpha,int(i)))
            for m in range(len(comb_list)):
                temp_cnt=0
                for j in orders:
                    check=True
                    for k in range(len(comb_list[m])):
                        if comb_list[m][k] not in j:
                            check=False
                            break
                    if check:
                        temp_cnt+=1
                if temp_cnt>max_cnt and temp_cnt>=2:
                    max_cnt=temp_cnt
                    temp_res=[comb_list[m]]
                elif temp_cnt==max_cnt and temp_cnt>=2:
                    temp_res.append(comb_list[m])
            for j in range(len(temp_res)):
                answer.append(temp_res[j])

    answer.sort()
    for i in range(len(answer)):
        answer[i]="".join(sorted(answer[i]))
    return answer

#orders=[["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],["XYZ", "XWY", "WXA"]]
orders=[["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],["XYZ", "XWY", "WXA"]]

course=[[2,3,4],[2,3,5],[2,3,4]]
for i in range(len(orders)):
    print(solution(orders[i], course[i]))
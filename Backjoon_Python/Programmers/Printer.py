#프린터
def solution(priorities, location):
    answer = 0
    while len(priorities)>0:        #대기 목록에 문서가 있는 동안 반복
        temp=priorities.pop(0)      #첫 번째 문서 꺼내기
        if len(priorities)==0:      #껴낸 문서가 마지막 일때 종료
            answer+=1
        else:
            if temp>=max(priorities):   #꺼낸 문서의 중요도가 제일 높을 때
                if location==0:         #찾고자 하는 문서일 때 종료
                    answer+=1
                    break
                else:
                    location-=1
                    answer+=1
                        
            #꺼낸 문서보다 중요도가 높은 문서가 대기 목록에 존재할 때
            else:
                priorities.append(temp)
                location-=1
                if location<0:
                    location=len(priorities)-1
    return answer

priorities=[[3,2,3,4,5],[5,4,3,2,1]]
location=[2,2]

for i in range(len(priorities)):
    print(solution(priorities[i], location[i]))

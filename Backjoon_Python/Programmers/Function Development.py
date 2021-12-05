#기능개발
def solution(progresses, speeds):
    answer = []
    day=0           #개발 일수
    curr_index=0    #작업 Index

    #작업 Index를 0번 부터 끝까지 반복
    while curr_index<len(progresses):

        #현재 작업이 100% 넘을 때까지 day 증가
        while progresses[curr_index]+speeds[curr_index]*day<100:
            day+=1

        #완료된 작업 개수 카운트
        cnt=0

        #완료된 작업 카운트
        while curr_index<len(progresses) and progresses[curr_index]+speeds[curr_index]*day>=100:
            cnt+=1
            curr_index+=1
        answer.append(cnt)
    return answer

progresses=[[93, 30, 55],[95, 90, 99, 99, 80, 99]]
speeds=[[1, 30, 5],[1, 1, 1, 1, 1, 1]]

for i in range(len(progresses)):
    print(solution(progresses[i], speeds[i]))
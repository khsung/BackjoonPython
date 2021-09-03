#추석 트래픽
def solution(lines):
    answer=1

    for i in range(len(lines)):
        temp=list(lines[i].split())
        temp[1]=temp[1].split(":")
        temp_s=int(temp[1][0])*3600+int(temp[1][1])*60+float(temp[1][2])
        lines[i]=[round(temp_s+0.001-float(temp[2][:-1]),3),temp_s]
    
    for i in range(len(lines)-1):
        end_time=lines[i][1]
        cnt=1
        for j in range(i+1,len(lines)):
            if lines[j][1]>end_time+4:
                break
            elif lines[j][0]<end_time+1:
                cnt+=1
        if answer<cnt:
            answer=cnt
    return answer

lines=[["2016-09-15 01:00:04.001 2.0s","2016-09-15 01:00:07.000 2s"],["2016-09-15 01:00:04.002 2.0s","2016-09-15 01:00:07.000 2s"],["2016-09-15 20:59:57.421 0.351s","2016-09-15 20:59:58.233 1.181s","2016-09-15 20:59:58.299 0.8s","2016-09-15 20:59:58.688 1.041s","2016-09-15 20:59:59.591 1.412s","2016-09-15 21:00:00.464 1.466s","2016-09-15 21:00:00.741 1.581s","2016-09-15 21:00:00.748 2.31s","2016-09-15 21:00:00.966 0.381s","2016-09-15 21:00:02.066 2.62s"]]
for i in range(len(lines)):
    print(solution(lines[i]))
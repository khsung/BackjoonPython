#셔틀버스
def solution(n, t, m, timetable):
    answer = 0
    for i in range(len(timetable)):
        temp=list(map(int,timetable[i].split(":")))
        timetable[i]=temp[0]*60+temp[1]
    timetable.sort()
    curr_time=540
    curr_index=0
    for i in range(n):
        for j in range(m):
            if i==n-1 and j==m-1:
                if curr_index>=len(timetable) or timetable[curr_index]>curr_time:
                    answer=curr_time
                elif timetable[curr_index]<=curr_time:
                    answer=timetable[curr_index]-1

            else:
                if curr_index<len(timetable) and timetable[curr_index]<=curr_time:
                    answer=timetable[curr_index]-1
                    curr_index+=1
                    
        curr_time+=t
    answer=str(answer//60).zfill(2)+":"+str(answer%60).zfill(2)
    return answer

n=[1,2,2,1,1,10]
t=[1,10,1,1,1,60]
m=[5,2,2,5,1,45]
timetable=[["08:00", "08:01", "08:02", "08:03"],["09:10", "09:09", "08:00"],["09:00", "09:00", "09:00", "09:00"],["00:01", "00:01", "00:01", "00:01", "00:01"],	["23:59"],["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]]
for i in range(len(n)):
    print(solution(n[i], t[i], m[i], timetable[i]))
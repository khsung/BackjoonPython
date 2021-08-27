#오픈채팅방
def solution(record):
    answer = []
    temp_res=[]
    user_nick={}
    for i in range(len(record)):
        record[i]=list(record[i].split())
        if record[i][0]=="Enter":
            user_nick[record[i][1]]=record[i][2]
            temp_res.append([record[i][1],"님이 들어왔습니다."])
        elif record[i][0]=="Leave":
            temp_res.append([record[i][1],"님이 나갔습니다."])
        else:
            user_nick[record[i][1]]=record[i][2]
    for i in range(len(temp_res)):
        temp=user_nick[temp_res[i][0]]+temp_res[i][1]
        answer.append(temp)

    return answer

record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))
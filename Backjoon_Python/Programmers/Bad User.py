#불량 사용자
import copy
def backtracking(user_id, banned_id,curr_list):
    global answer,answer_list
    if len(curr_list)==len(banned_id):
        temp=copy.deepcopy(curr_list)
        temp.sort()
        if temp not in answer_list:
            temp.sort()
            answer_list.append(temp)
            answer+=1
    else:
        for i in range(len(user_id)):
            if len(user_id[i])==len(banned_id[len(curr_list)]) and user_id[i] not in curr_list: 
                check=True
                for j in range(len(user_id[i])):
                    if banned_id[len(curr_list)][j]!="*" and user_id[i][j]!=banned_id[len(curr_list)][j]:
                        check=False
                        break
                if check:
                    curr_list.append(user_id[i])
                    backtracking(user_id, banned_id,curr_list)
                    curr_list.pop()

def solution(user_id, banned_id):
    global answer_list,answer
    answer = 0
    answer_list=[]
    curr_list=[]
    for i in range(len(user_id)):
        if len(user_id[i])==len(banned_id[0]):
            check=True
            for j in range(len(user_id[i])):
                if banned_id[0][j]!="*" and  user_id[i][j]!=banned_id[0][j]:
                    check=False
                    break
            if check:
                curr_list.append(user_id[i])
                backtracking(user_id, banned_id,curr_list)
                curr_list.pop()

    return answer
    
user_id=[["frodo", "fradi", "crodo", "abc123", "frodoc"],["frodo", "fradi", "crodo", "abc123", "frodoc"],["frodo", "fradi", "crodo", "abc123", "frodoc"]]
banned_id=[["fr*d*", "abc1**"],["*rodo", "*rodo", "******"],["fr*d*", "*rodo", "******", "******"]]
for i in range(len(user_id)):
    print(solution(user_id[i], banned_id[i]))
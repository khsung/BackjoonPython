#불량 사용자
import copy
def solution(user_id, banned_id):
    global answer,answer_list
    answer = 0
    answer_list=[]
    backtracking(user_id, banned_id,0,[])
    return answer

def backtracking(user_id, banned_id,curr_index,result):
    global answer,answer_list
    print(result,curr_index)
    if curr_index==len(banned_id):
        result.sort()
        answer_list.sort()
        if result not in answer_list:
            answer+=1
            temp=copy.deepcopy(result)
            answer_list.append(temp)
            
    else:
        for i in user_id:
            if len(i)==len(banned_id[curr_index]) and i not in result:
                check=True
                for j in range(len(i)):
                    if banned_id[curr_index][j]!="*" and banned_id[curr_index][j]!=i[j]:
                        check=False
                        break
                if check:
                    result.append(i)
                    backtracking(user_id, banned_id,curr_index+1,result)
                    result.pop()
    
    
#user_id=[["frodo", "fradi", "crodo", "abc123", "frodoc"],["frodo", "fradi", "crodo", "abc123", "frodoc"],["frodo", "fradi", "crodo", "abc123", "frodoc"]]
#banned_id=[["fr*d*", "abc1**"],["*rodo", "*rodo", "******"],["fr*d*", "*rodo", "******", "******"]]
user_id=[["frodo", "fradi", "crodo", "abc123", "frodoc"]]
banned_id=[["fr*d*", "*rodo", "******", "******"]]
for i in range(len(user_id)):
    print(solution(user_id[i], banned_id[i]))
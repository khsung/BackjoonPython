#후보키
def backtracking(relation,curr_len,visited,res_list,curr_index,temp_res):
    #print(temp_res)
    if len(temp_res)==curr_len:
        check=True
        for i in range(len(relation)-1):
            for j in range(i+1,len(relation)):
                cnt=0
                for k in range(len(temp_res)):
                    if relation[i][temp_res[k]]==relation[j][temp_res[k]]:
                        cnt+=1
                if cnt==curr_len:
                    check=False
                if not check:
                    break
            if not check:
                break
        if check:
            res_list.append([])
            for i in range(len(temp_res)):
                res_list[-1].append(temp_res[i])
                visited[temp_res[i]]=1
    else:
        for i in range(len(visited)):
            if visited[i]==0 and i not in temp_res:
                temp_res.append(i)
                backtracking(relation,curr_len,visited,res_list,curr_index,temp_res)
                temp_res.pop()

def solution(relation):
    res_list=[]
    curr_len=1
    visited=[0 for i in range(len(relation[0]))]
    while curr_len<=visited.count(0):
        for i in range(len(visited)):
            temp_res=[]
            if visited[i]==0:
                temp_res.append(i)
                backtracking(relation,curr_len,visited,res_list,i,temp_res)
                temp_res.pop()

        curr_len+=1
    return len(res_list)

#relation=[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
relation=[['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]
print(solution(relation))
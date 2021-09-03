#표 편집
from collections import deque
def solution(n, k, cmd):
    answer = ["O" for i in range(n)]
    deleted=[]
    left=deque([i for i in range(k)])
    right=deque([i for i in range(k,n)])
    for i in range(len(cmd)):
        if len(cmd[i])==1:
            if cmd[i]=="C":
                deleted.append(right.popleft())
                if len(right)==0:
                    try:
                        right.append(left.pop())
                    except:
                        pass
            else:
                temp=deleted.pop()
                check=True
                if temp<right[0]:
                    for j in range(len(left)):
                        if left[j]<temp:
                            left.insert(j,temp)
                            check=False
                            break
                    if check:
                        left.append(temp)
                else:
                    for j in range(len(right)):
                        if right[j]<temp:
                            right.insert(j,temp)
                            check=False
                            break
                    if check:
                        right.append(temp)
        else:
            if cmd[i][0]=="U":
                for j in range(int(cmd[i][2])):
                    right.appendleft(left.pop())
            else:
                for j in range(int(cmd[i][2])):
                    left.append(right.popleft())
    for i in range(len(deleted)):
        answer[deleted[i]]="X"
    answer="".join(answer)
    return answer

#n=[8,8]
#k=[2,2]
#cmd=[["D 2","C","U 3","C","D 4","C","U 2","Z","Z"],["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]]
n=[8]
k=[0]
cmd=[["C","C","C","C","C","C","C","C"]]
for i in range(len(n)):
    print(solution(n[i], k[i], cmd[i]))
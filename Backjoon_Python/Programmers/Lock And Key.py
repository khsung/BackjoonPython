#자물쇠와 열쇠
def trans(key):
    #90도 시계방향 회전
    for i in range(len(key)//2):
        key[i],key[len(key)-1-i]=key[len(key)-1-i],key[i]

    for i in range(len(key)):
        for j in range(i+1,len(key[i])):
            key[i][j],key[j][i]=key[j][i],key[i][j]
    return key

def findzero(key,key_list):
    temp_list=[]
    for i in range(len(key)):
        for j in range(len(key[i])):
            if key[i][j]==1:
                temp_list.append([i,j])
    return temp_list

def solution(key, lock):
    answer = False
    key_list=[]
    lock_list=[]
    for i in range(len(lock)):
        for j in range(len(lock[i])):
            if lock[i][j]==0:
                lock_list.append([i,j])

    for i in range(4):
        key=trans(key)
        key_list=findzero(key,key_list)
        for j in range(len(key_list)-len(lock_list)+1):
            x_diff=key_list[j][0]-lock_list[0][0]
            y_diff=key_list[j][1]-lock_list[0][1]
            for k in range(1,len(lock_list)):
                if x_diff!=key_list[j+k][0]-lock_list[k][0] or y_diff!=key_list[j+k][1]-lock_list[k][1]:
                    break
                else:
                    if len(lock_list)-1==k:
                        return True

    return answer

key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))
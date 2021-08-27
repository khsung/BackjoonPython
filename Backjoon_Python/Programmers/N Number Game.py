#n진수 게임
def solution(n, t, m, p):
    answer = ''
    numbers=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    curr_num=[0]
    curr_index=len(curr_num)-1
    for i in range(t):
        for j in range(m):
            if j==p-1:
                answer+=numbers[curr_num[curr_index]]
            if curr_index>0:
                curr_index-=1
            else:
                curr_num[0]+=1
                if curr_num[0]>=n:
                    try:
                        curr=0
                        while curr_num[curr]>=n:
                            curr_num[curr]=curr_num[curr]%n
                            curr_num[curr+1]+=1
                            curr+=1
                    except:
                        curr_num.append(1)
                curr_index=len(curr_num)-1
    return answer

n=[2,16,16]
t=[4,16,16]
m=[2,2,2]
p=[1,1,2]

for i in range(len(n)):
    print(solution(n[i], t[i], m[i], p[i]))
#print(solution(n[0], t[0], m[0], p[0]))
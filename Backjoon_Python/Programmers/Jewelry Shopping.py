#보석 쇼핑
def solution(gems):
    gem=[0 for i in range(26)]
    curr_gem=[0 for i in range(26)]
    distance=len(gems)
    cnt=0
    curr_cnt=0
    left=0
    right=0
    left_res=1
    right_res=len(gems)
    #True일때 right증가, False일때 left증가
    check=True
    #print(ord("A")-65)
    #print(ord("Z")-65)

    for i in range(len(gems)):
        for j in range(len(gems[i])):
            if gem[ord(gems[i][j])-65]==0:
                gem[ord(gems[i][j])-65]=1
                cnt+=1
    print(curr_gem,curr_cnt,cnt,left_res,right_res)
    while right<len(gems):
        #print(left,right,distance)
        #print(curr_gem,curr_cnt,cnt,left_res,right_res)
        if check:
            for i in range(len(gems[right])):
                curr_gem[ord(gems[right][i])-65]+=1
                if curr_gem[ord(gems[right][i])-65]==1:
                    curr_cnt+=1
            if curr_cnt==cnt:
                if distance>right-left+1:
                    distance=right-left+1
                    left_res=left+1
                    right_res=right+1
                if left<right:
                    left+=1
                    check=False
                else:
                    right+=1
                    check=True
            else:
                right+=1
        else:
            print(left)
            for i in range(len(gems[left])):
                curr_gem[ord(gems[left][i])-65]-=1
                if curr_gem[ord(gems[left][i])-65]==0:
                    curr_cnt-=1
            if curr_cnt==cnt:
                if distance>right-left+1:
                    distance=right-left+1
                    left_res=left+1
                    right_res=right+1
                if left<right:
                    left+=1
                else:
                    right+=1
                    check=True
            else:
                right+=1
                check=True
        print(curr_gem,curr_cnt,cnt,left_res,right_res)
    answer=[left_res,right_res]
    return answer

gems=[["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],["AA", "AB", "AC", "AA", "AC"],["XYZ", "XYZ", "XYZ"],["ZZZ", "YYY", "NNNN", "YYY", "BBB"]]

for i in range(len(gems)):
    print(solution(gems[i]))

    #A=65, Z=90
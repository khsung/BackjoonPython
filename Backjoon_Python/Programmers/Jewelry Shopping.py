#보석 쇼핑
def solution(gems):
    answer = [1,len(gems)]
    answer_len=len(gems)
    curr_gems=[0 for i in range(26)]
    alpha=[0 for i in range(26)]
    for i in gems:
        for j in i:
            if alpha[ord(j)-ord("A")]==0:
                alpha[ord(j)-ord("A")]=1

    left=0
    right=0
    add=True
    while right<len(gems) and left<=right:
        print(curr_gems,add)
        print(alpha,left,right)
        if add:
            for i in gems[right]:
               curr_gems[ord(i)-ord("A")]+=1
               alpha[ord(i)-ord("A")]=0
            if alpha.count(1)==0:
                if right-left+1<answer_len:
                    answer_len=right-left+1
                    answer=[left+1,right+1]
                add=False
            else:
                right+=1

        else:
            for i in gems[left]:
                curr_gems[ord(i)-ord("A")]-=1
                if curr_gems[ord(i)-ord("A")]==0:
                    alpha[ord(i)-ord("A")]=1
            left+=1
            if alpha.count(1)==0:
                if right-left+1<answer_len:
                    answer_len=right-left+1
                    answer=[left+1,right+1]
                left+=1
            else:
                right+=1
                add=True
    return answer

gems=[["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],["AA", "AB", "AC", "AA", "AC"],["XYZ", "XYZ", "XYZ"],["ZZZ", "YYY", "NNNN", "YYY", "BBB"]]
#gems=[["ZZZ", "YYY", "NNNN", "YYY", "BBB"]]
for i in range(len(gems)):
    print(solution(gems[i]))

    #A=65, Z=90

#110 옮기기
def solution(s):
    answer = []
    for i in range(len(s)):
        left=""
        mid=""
        right=""
        for j in s[i]:
            if j=="0":
                if len(right)>=2:
                    right=right[:-2]
                    mid+="110"
                else:
                    left+=j
            else:
                right+=j
        answer.append(left+mid+right)

    return answer

s=["1110","100111100","0111111010"]
print(solution(s))
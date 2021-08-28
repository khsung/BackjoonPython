#문자열 압축
def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        temp=""
        cnt=1
        for j in range(i,len(s),i):
            if s[j:j+i]==s[j-i:j]:
                cnt+=1
            else:
                if cnt==1:
                    temp+=s[j-i:j]
                else:
                    temp+=(str(cnt)+s[j-i:j])
                    cnt=1
            last=j
        if cnt==1:
            temp+=s[last:]
        else:
            temp+=(str(cnt)+s[len(s)-i:])
        if len(temp)<answer:
            answer=len(temp)

    return answer

s=["aabbaccc","ababcdcdababcdcd","abcabcdede","abcabcabcabcdededededede","xababcdcdababcdcd"]

for i in range(len(s)):
    print(solution(s[i]))

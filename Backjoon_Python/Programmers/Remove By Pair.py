#짝지어 제거하기
def solution(s):
    answer = 0
    stack=[]
    for i in s:
        if len(stack)==0:
            stack.append(i)
        elif stack[len(stack)-1]==i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack)==0:
        answer=1
    return answer

s=["baabaa","cdcd"]
for i in range(len(s)):
    print(solution(s[i]))
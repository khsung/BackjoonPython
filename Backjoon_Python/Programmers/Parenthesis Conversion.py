#괄호 변환
def divide_str(s):
    u=v=""
    left_str=right_str=0
    for i in range(len(s)):
        if s[i]=="(":
            left_str+=1
        else:
            right_str+=1
        if left_str==right_str:
            u=s[:i+1]
            v=s[i+1:]
            break
    return u,v

def check_match(u):
    stack=[]
    for i in u:
        if i=="(":
            stack.append("(")
        else:
            if len(stack)>0 and stack.pop()=="(":
                pass
            else:
                return False
    return True

def return_res(p):
    u,v=divide_str(p)
    if len(u)>0 and check_match(u):
        res=u+return_res(v)
        return res
    elif len(u)==0:
        return u
    else:
        temp="("+return_res(v)
        temp=temp+u[::-1][1:-1]+")"
        return temp

def solution(p):
    answer = ''
    if check_match(p):
        return p
    else:
        answer=return_res(p)

    return answer

p=[")))(((",")(","()))((()","(()())()"]
for i in range(len(p)):
    print(solution(p[i]))
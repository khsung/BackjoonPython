#괄호 변환
def correct(s):
    queue=[]
    for i in s:
        if i=="(":
            queue.append(i)
        else:
            if len(queue)==0:
                return False
            else:
                queue.pop()
    if len(queue)==0:
        return True
    else:
        return False

def first(p):
    if len(p)==0:
        return p
    else:
        left=0
        right=0
        for i in range(len(p)):
            if p[i]=="(":
                left+=1
            elif p[i]==")":
                right+=1
            if left==right:
                u=p[:i+1]
                v=p[i+1:]
                break
        if correct(u):
            return u+first(v)
        else:
            temp="("+first(v)+")"
            for i in range(1,len(u)-1):
                if u[i]=="(":
                    temp+=")"
                else:
                    temp+="("
            return temp

def solution(p):
    return first(p)

p=["(()())()",")(","()))((()","))()(("]
for i in range(len(p)):
    print(solution(p[i]))
#1662 압축
#s=input()
#stack=[]
#for i in s:
#    if i==")":
#        temp_s=''
#        while stack[len(stack)-1]!="(":
#            temp_s=stack[len(stack)-1]+temp_s
#            stack.pop()
#        stack.pop()
#        stack[len(stack)-1]=int(stack[len(stack)-1])*temp_s
#        if len(stack[len(stack)-1])==0:
#            stack.pop()
#    else:
#        stack.append(i)
#res=0
#for i in stack:
#    res+=len(i)
#print(res)


def recur(s):
    temp=""
    for i in range(len(s)):
        if s[i]=="(":
            a=recur(s[i+1:])
            return (len(temp)-1)+((int(temp)%10)*a)
        elif s[i]==")":
            return len(temp)+recur(s[i+1:])
        else:
            temp=temp+s[i]
    return len(temp)
s=list(input())
print(recur(s))
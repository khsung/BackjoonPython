#11723 집합
dic={}
n=int(input())
temp_dic={}
for i in range(20):
    temp_dic[i+1]=1
for i in range(n):
    option=list(input().split())
    if len(option)==2:
        num=int(option[1])
        if option[0]=="add":
            if num not in dic:
                dic[num]=1
        elif option[0]=="remove":
            if num in dic:
                del dic[num]
        elif option[0]=="check":
            if num in dic:
                print(dic[num])
            else:
                print(0)
        elif option[0]=="toggle":
            if num in dic:
                del dic[num]
            else:
                dic[num]=1
    else:
        if option[0]=="all":
            dic=temp_dic.copy()
        else:
            dic={}
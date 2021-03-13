#1406 에디터 시간초과 단순 리스트방식으론 안됨
import sys
string=list(sys.stdin.readline().rstrip('\n'))
n=int(input())
cursor=len(string)
res=""
for i in range(n):
    temp=sys.stdin.readline().rstrip('\n')
    if temp[0]=="L":
        if cursor>0:
            cursor-=1
    elif temp[0]=="D":
        if cursor<len(string):
            cursor+=1
    elif temp[0]=="B":
        if cursor>0:
            del string[cursor-1]
            cursor-=1
    else:
        string.insert(cursor,temp[2])
        cursor+=1
for i in string:
    res+=i
print(res)
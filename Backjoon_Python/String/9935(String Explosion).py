#9935 문자열 폭발
import sys
first=list(sys.stdin.readline().split())
second=list(sys.stdin.readline().split())
temp_stack=[]
for i in first:
    if i in second:
        pass
    else:
        temp_stack.append(i)
if len(first[0])==0:
    print("FRULA")
else:
    print(first[0])
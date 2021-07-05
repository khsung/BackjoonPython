#9935 문자열 폭발
import sys
first=list(sys.stdin.readline().split())
second=list(sys.stdin.readline().split())
while second[0] in first[0]:
    first[0]=first[0].replace(second[0],"")
if len(first[0])==0:
    print("FRULA")
else:
    print(first[0])
#17219 비밀번호 찾기
import sys
n,m=map(int,input().split())
dic={}
for i in range(n):
    temp=list(sys.stdin.readline().split())
    dic[temp[0]]=temp[1]
for i in range(m):
    q=sys.stdin.readline().split()
    print(dic[q[0]])
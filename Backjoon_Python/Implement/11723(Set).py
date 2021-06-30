#11723 집합
import sys
n=int(input())
S=[0 for i in range(20)]
for i in range(n):
    op=sys.stdin.readline().split()
    if len(op)==1:
        if op[0]=='all':
            S=[1 for i in range(20)]
        else:
            S=[0 for i in range(20)]
    else:
        if op[0]=='add':
            S[int(op[1])-1]=1
        elif op[0]=='remove':
            S[int(op[1])-1]=0
        elif op[0]=='check':
            print(S[int(op[1])-1])
        else:
            S[int(op[1])-1]=(S[int(op[1])-1]+1)%2
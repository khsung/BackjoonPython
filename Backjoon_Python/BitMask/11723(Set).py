#11723 집합
import sys
S=0
n=int(input())
for i in range(n):
    op=sys.stdin.readline().split()
    if len(op)==1:
        if op[0]=="all":
            S=2**20-1
        elif op[0]=="empty":
            S=0
    else:
        if op[0]=="add":
            S=S|2**(int(op[1])-1)
        elif op[0]=="remove":
            S=S&~2**(int(op[1])-1)
        elif op[0]=="check":
            temp=bin(S&2**(int(op[1])-1))
            if len(temp)-2>=int(op[1]) and temp[-1*int(op[1])]=="1":
                print(1)
            else:
                print(0)
        elif op[0]=="toggle":
            S=S^2**(int(op[1])-1)
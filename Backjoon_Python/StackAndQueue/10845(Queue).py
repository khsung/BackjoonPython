#10845 큐
import sys
n=int(input())
queue=[]
for i in range(n):
    op=list(sys.stdin.readline().split())
    if op[0]=="push":
        queue.append(op[1])
    elif op[0]=="pop":
        if len(queue)==0:
            print(-1)
        else:
            print(queue.pop(0))
    elif op[0]=="size":
        print(len(queue))
    elif op[0]=="empty":
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif op[0]=="front":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue)==0:
            print(-1)
        else:
            print(queue[len(queue)-1])
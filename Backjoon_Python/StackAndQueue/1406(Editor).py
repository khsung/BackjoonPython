#1406 에디터
import sys
left_stack=list(sys.stdin.readline().strip())
right_stack=[]
num=int(input())
for i in range(num):
    command=sys.stdin.readline().strip()
    if len(command)==3:
        cmd=command.split()
        left_stack.append(cmd[1])
    else:
        if command=="L":
            if len(left_stack)!=0:
                right_stack.append(left_stack.pop())
        elif command=="D":
            if len(right_stack)!=0:
                left_stack.append(right_stack.pop())
        else:
            if len(left_stack)!=0:
                left_stack.pop()
left_stack=left_stack+list(reversed(right_stack))
for i in left_stack:
    print(i,end="")
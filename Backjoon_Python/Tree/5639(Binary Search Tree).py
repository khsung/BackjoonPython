#5639 이진 검색 트리
from collections import deque
import sys
sys.setrecursionlimit(10 ** 8)

def postorder(index):
    global tree
    if tree[2*index]!=0:
        postorder(2*index)
    if tree[2*index+1]!=0:
        postorder(2*index+1)
    print(tree[index])

tree=[0 for i in range(500000)]
data=deque()
while True:
    try:
        data.append(int(input()))
    except:
        break

if len(data)>0:
    prev_stack=[]
    prev_stack.append([data.popleft(),1])
    tree[1]=prev_stack[0][0]
    curr_index=1
    while len(data)>0:
        temp=data.popleft()
        if len(prev_stack)>0 and prev_stack[len(prev_stack)-1][0]>temp:
            curr_index=curr_index*2
            tree[curr_index]=temp
            prev_stack.append([temp,curr_index])
        else:
            while len(prev_stack)>0 and prev_stack[len(prev_stack)-1][0]<temp:
                temp1=prev_stack.pop()
            curr_index=temp1[1]*2+1
            tree[curr_index]=temp
            prev_stack.append([temp,curr_index])

    postorder(1)
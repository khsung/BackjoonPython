#1874 Stack Sequence
sequence=[]
stack=[]
op=[]
num=int(input())
for i in range(num):
    x=int(input())
    sequence.append(x)

for i in range(1,max(sequence)+1):
    stack.append(i)
    op.append('+')
    while len(stack)>0 and sequence[0]==stack[-1]:
        sequence.pop(0)
        stack.pop()
        op.append('-')
if len(stack)==0:
    for i in range(len(op)):
        print(op[i])
else:
    print("NO")


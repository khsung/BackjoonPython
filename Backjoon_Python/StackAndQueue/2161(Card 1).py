#2161 카드 1
size=int(input())
queue=[i for i in range(1,size+1)]
while len(queue)>1:
    print(queue.pop(0),end=" ")
    queue.append(queue.pop(0))
print(queue[0])
#스택과 큐 구현
#stack=[]    #스택 선언
#print("현재 스택 :",stack)
#stack.append(1)     # 1 추가
#print("현재 스택 :",stack)
#stack.append(2)     # 2 추가
#print("현재 스택 :",stack)
#stack.pop()         #끝 원소 하나 제거
#print("현재 스택 :",stack)
#stack.pop()         #끝 원소 하나 제거
#print("현재 스택 :",stack, end="\n\n")

#queue=[]    #큐 선언
#print("현재 큐 :",queue)
#queue.append(1)     # 1 추가
#print("현재 큐 :",queue)
#queue.append(2)     # 2 추가
#print("현재 큐 :",queue)
#queue.pop(0)         #첫 원소 하나 제거
#print("현재 큐 :",queue)
#queue.pop(0)         #첫 원소 하나 제거
#print("현재 큐 :",queue)

from collections import deque   #데크 모듈 선언
deque=deque()
print("현재 데크 :",deque)
deque.append(1)         #오른쪽에 1 추가
print("현재 데크 :",deque)
deque.appendleft(2)     #왼쪽에 2 추가
print("현재 데크 :",deque)
deque.popleft()         #첫 번째 원소 제거
print("현재 데크 :",deque)
deque.pop()             #끝 원소 제거
print("현재 데크 :",deque)
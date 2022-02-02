#15903 카드 합체 놀이
#n,m=map(int,input().split())
#card=list(map(int,input().split()))
#for i in range(m):
#    card.sort()
#    card[0],card[1]=card[0]+card[1],card[0]+card[1]

#print(sum(card))

import heapq

n,m=map(int,input().split())
card=list(map(int,input().split()))
heapq.heapify(card)
for i in range(m):
    tempa=heapq.heappop(card)
    tempb=heapq.heappop(card)
    heapq.heappush(card,tempa+tempb)
    heapq.heappush(card,tempa+tempb)

print(sum(card))

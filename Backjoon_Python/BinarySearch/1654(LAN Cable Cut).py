#1654 랜선 자르기
k,n=map(int,input().split())
cable=[]
for i in range(k):
    cable.append(int(input()))
cable.sort()
stand=cable[0]
for i in range(stand,0,-1):
    if k*(cable[len(cable)-1]//i)<n:
        pass
    else:
        cnt=0
        for j in cable:
            cnt=cnt+(j//i)
        if cnt==n:
            print(i)
            break
#17389 보너스 점수
n=int(input())
score=input()
bonus=0
res=0
for i in range(n):
    if score[i]=="O":
        res+=(i+1)
        res+=bonus
        bonus+=1
    else:
        bonus=0
print(res)
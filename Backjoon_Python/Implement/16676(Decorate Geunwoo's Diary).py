#16676 근우의 다이어리 꾸미기
n=int(input())
temp_n=n
stand=0
digit=0
while temp_n>0:
    temp_n=temp_n//10
    digit+=1
for i in range(digit):
    stand=stand*10+1
if n<10:
    print(1)
elif stand>n:
    print(digit-1)
else:
    print(digit)
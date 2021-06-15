#16676 근우의 다이어리 꾸미기
n=int(input())
num_array=[0 for i in range(10)]
while n>0:
    num_array[int(n%10)]+=1
    n=n//10
print(max(num_array))
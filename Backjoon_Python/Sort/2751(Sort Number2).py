
#2751 Sort Number2
num=int(input())
numbers=[]
for i in range(num):
    numbers.append(int(input()))
for i in sorted(numbers):
    print(i)
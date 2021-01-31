#2108 통계학
import sys
from collections import Counter
num=int(input())
max_num=-4001
min_num=4001
sum1=0
numbers=[]
first=0
many=0
for i in range(num):
    a=int(sys.stdin.readline())
    numbers.append(a)
    sum1+=a
    if min_num>a:
        min_num=a
    if max_num<a:
        max_num=a
numbers.sort()
avg=round(sum1/num)
print(avg)
print(numbers[int(num/2)])
temp=Counter(numbers).most_common()
if len(temp)>1:
    print(temp[1][0])
else:
    print(temp[0][0])
print(max_num-min_num)
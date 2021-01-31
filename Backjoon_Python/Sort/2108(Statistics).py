#2108 통계학

num=int(input())
max_num=-4001
min_num=4001
sum1=0
numbers=[]
first=0
count1=[0 for i in range(8001)]
many=0
for i in range(num):
    a=int(input())
    numbers.append(a)
    sum1+=a
    count1[a+4000]+=1
    if min_num>a:
        min_num=a
    if max_num<a:
        max_num=a
numbers.sort()
avg=round(sum1/num)
print(avg)
print(numbers[int(num/2)])
temp1=max(count1)
temp2=count1.index(max(count1))
count1[temp2]=0
if temp1==max(count1) and first == 0:
    first=1
    temp2=count1.index(max(count1))
print(temp2-4000)
print(max_num-min_num)
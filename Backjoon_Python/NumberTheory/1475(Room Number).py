#1475 방 번호
room=input()
array=[0 for i in range(10)]
for i in range(len(room)):
    array[int(room[i])]+=1
count6=array[6]
count9=array[9]
del array[9]
del array[6]
maxnum=max(array)
temp=count6+count9
if temp-2*maxnum<=0:
    print(maxnum)
else:
    if temp%2==1:
        temp+=1
    print(temp//2)
#7568 Bulk
num=int(input())
array=[]
rankarray=[0 for i in range(num)]
for i in range(num):
    a,b=input().split()
    array.append([int(a),int(b)])

for i in range(len(array)):
    count=0
    for j in range(len(array)):
        if array[i][0]<array[j][0] and array[i][1]<array[j][1]:
            count+=1
    rankarray[i]=count+1
for i in range(len(rankarray)):
    print(rankarray[i],end=" ")
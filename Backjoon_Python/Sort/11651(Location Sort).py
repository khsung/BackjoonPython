#11651 Location Sort
num=int(input())
array=[]
for i in range(num):
    a,b=input().split()
    array.append([int(a),int(b)])
sorted_array=sorted(array, key=lambda x:(x[1],x[0]))
for i in range(len(sorted_array)):
    print(sorted_array[i][0],sorted_array[i][1])

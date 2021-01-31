#11650 Location Sort

num = int(input())
location=[]
for i in range(num):
    a, b=input().split()
    location.append([int(a),int(b)])
location.sort()
for i in range(len(location)):
    print(location[i][0],location[i][1])


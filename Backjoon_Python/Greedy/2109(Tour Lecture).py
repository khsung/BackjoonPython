#2109 순회강연(틀림)
num = int(input())
array = []
sum = 0
day = 0
for i in range(num):
    a,b = map(int,input().split())
    array.append([a,b])
array = sorted(array, key=lambda x:(x[1],-x[0]))
while len(array) > 0:
    day+=1
    sum+=array[0][0]
    array.pop(0)
    while len(array) > 0 and day == array[0][1]:
        array.pop(0)
print(sum)
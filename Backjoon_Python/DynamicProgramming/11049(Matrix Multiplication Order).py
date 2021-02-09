#11049 행렬 곱셈 순서
import sys
num=int(input())
matrix=[]
sum=0
for i in range(num):
    a,b=sys.stdin.readline().split()
    matrix.append([int(a),int(b)])
while len(matrix)>1:
    min=1250000000
    for i in range(len(matrix)-1):
        temp=matrix[i][0]*matrix[i][1]*matrix[i+1][1]
        if min>temp:
            min=temp
            minindex=i
    sum+=min
    matrix.insert(minindex,[matrix[minindex][0],matrix[minindex+1][1]])
    del matrix[minindex+1]
    del matrix[minindex+1]
print(sum)
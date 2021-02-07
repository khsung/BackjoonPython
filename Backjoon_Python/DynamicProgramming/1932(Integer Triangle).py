#1932 정수 삼각형
num = int(input())
triangle = []
row = 2
for i in range(num):
    number = list(map(int,input().split()))
    triangle.append(number)

for i in range(1,len(triangle)):
    for j in range(row):
        if j==0:
            triangle[i][j]+=triangle[i-1][j]
        elif j==(row-1):
            triangle[i][j]+=triangle[i-1][j-1]
        else:
            if triangle[i-1][j]>triangle[i-1][j-1]:
                triangle[i][j]+=triangle[i-1][j]
            else:
                triangle[i][j]+=triangle[i-1][j-1]
    row+=1
print(max(triangle[num-1]))
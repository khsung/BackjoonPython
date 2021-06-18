#2217 로프
n=int(input())
rope=[]
max_sum=0
for i in range(n):
    rope.append(int(input()))
rope.sort(reverse=True)

for i in range(n):
    if rope[i]*(i+1)>max_sum:
        max_sum=rope[i]*(i+1)
print(max_sum)
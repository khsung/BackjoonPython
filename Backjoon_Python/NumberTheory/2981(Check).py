#2981 검문
num = int(input())
num_list = []
M = []
for i in range(num):
    num_list.append(int(input()))
num_list.sort()
for i in range(2,num_list[len(num_list)-1] + 1):
    for j in range(len(num_list)):
        if j == 0:
            temp = num_list[j] % i
        else:
            if temp != num_list[j] % i:
                break
        if j == len(num_list) - 1:
            M.append(i)
for i in range(len(M)):
    print(M[i],end=" ")
#15829 Hashing
n=int(input())
degree=0
string=input()
res=0

for i in range(n):
    res=(res+(ord(string[i])-96)*31**degree)%1234567891
    degree+=1
print(res)
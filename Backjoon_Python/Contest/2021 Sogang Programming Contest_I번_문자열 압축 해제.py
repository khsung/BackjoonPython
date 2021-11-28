#I번 - 문자열 압축 해제
n=int(input())
word={}
res=""
for i in range(n):
    temp=list(input().split())
    word[temp[1]]=temp[0]
question=input()

for i in question:
    res+=word[i]
num=list(map(int,input().split()))
print(res[num[0]-1:num[1]])
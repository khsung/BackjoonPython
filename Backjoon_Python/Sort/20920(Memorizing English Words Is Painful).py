#20920 영단어 암기는 괴로워
import sys
word_check={}
n,m=map(int,sys.stdin.readline().split())
for i in range(n):
    temp=sys.stdin.readline().rstrip()
    if len(temp)>=m:
        if temp not in word_check:
            word_check[temp]=1
        else:
            word_check[temp]+=1

word_check=sorted(word_check.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))
for i in word_check:
    print(i[0])
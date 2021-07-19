#1062 가르침
n,k=map(int,input().split())
word=[]
res=0
alpha=[0 for i in range(26)]
alpha[ord('a')-97]=1
alpha[ord('n')-97]=1
alpha[ord('t')-97]=1
alpha[ord('i')-97]=1
alpha[ord('c')-97]=1
for i in range(n):
    temp=input()
    temp=temp[4:-4]
    temp=temp.replace("a","")
    temp=temp.replace("n","")
    temp=temp.replace("t","")
    temp=temp.replace("i","")
    temp=temp.replace("c","")
    word.append(temp)
if k<5:
    print(0)
else:
    k-=5
    for i in range(len(word)):
        word[i]=set(word[i])
        word[i]=list(word[i])
    word.sort(key=lambda x:(len(x),x))
    for i in range(len(word)):
        tempcnt=0
        for j in range(len(word[i])):
            if alpha[ord(word[i][j])-97]==0:
                alpha[ord(word[i][j])-97]=1
                tempcnt+=1
        if k<tempcnt:
            break
        else:
            k-=tempcnt
            res+=1
    print(res)

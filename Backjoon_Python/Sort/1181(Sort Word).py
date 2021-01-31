#1181 Sort word
num=int(input())
wordset=[]
for i in range(num):
    wordset.append(input())
sorted_wordset=sorted(wordset, key=lambda x:(len(x),x))
newarray=[]
for i in range(len(sorted_wordset)):
    if sorted_wordset[i] not in newarray:
        newarray.append(sorted_wordset[i])
for i in range(len(newarray)):
    print(newarray[i])
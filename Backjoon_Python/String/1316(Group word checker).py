
#그룹 단어 체커

num = int(input())
count=0
for i in range(num):
    check = [0 for i in range(26)]
    wordindex = 0
    word = input()
    while wordindex < len(word):
        if check[ord(word[wordindex])-ord('a')] == 1:
            break
        elif wordindex==len(word)-1 and check[ord(word[wordindex])-ord('a')]==0:
            count+=1
            wordindex+=1
        else:
            check[ord(word[wordindex])-ord('a')] = 1
            if wordindex < (len(word)-1) and word[wordindex]==word[wordindex+1]:
                check[ord(word[wordindex])-ord('a')] = 0
                wordindex+=1
            else:
                wordindex+=1
print(count)
#4358 생태학
import operator,sys
dic={}
cnt=0
while True:
    word=sys.stdin.readline().strip()
    if not word:
        break
    else:
        cnt+=1
        if word in dic:
            dic[word]+=1
        else:
            dic[word]=1


sorted_dic=sorted(dic.items(),key=operator.itemgetter(0))
for i in sorted_dic:
    print(i[0],round((100*i[1])/cnt,4))
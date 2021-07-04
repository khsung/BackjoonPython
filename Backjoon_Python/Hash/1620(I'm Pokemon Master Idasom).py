#1620 나는야 포켓몬 마스터 이다솜
n,m=map(int,input().split())
dic={}
num=1
for i in range(n):
    dic[input()]=num
    num+=1
res_list=list(dic.keys())
for i in range(m):
    q=input()
    if q.isdigit():
        print(res_list[int(q)-1])
    else:
        print(dic[q])
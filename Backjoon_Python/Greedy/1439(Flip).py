#1439 뒤집기
arr=list(map(int,input()))
check=-1
cnt=[0,0]
for i in arr:
    if i!=check:
        check=i
        cnt[i]+=1
if cnt[0]>cnt[1]:
    print(cnt[1])
else:
    print(cnt[0])
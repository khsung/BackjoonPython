#9663 N-Queen (시간초과)
n=int(input())

queen=[]
cnt=0
def check_queen(currx,curry):
    global queen
    check=True
    for i in queen:
        if i[0]==currx or abs(currx-i[0])==abs(curry-i[1]):
            check=False
            break
    if check:
        return True
    else:
        return False

def find_path(currx,curry):
    global n,cnt
    if curry<n-1:
        for i in range(n):
            if check_queen(i,curry):
                
                queen.append([i,curry])
                find_path(i,curry+1)
                queen.pop()
    else:
        for i in range(n):
            if check_queen(i,curry):
                cnt+=1

for i in range(n):
    queen.append([i,0])
    find_path(i,1)
    queen.pop()
print(cnt)
#2630 색종이 만들기


color = [0,0]
square = []
def findsquare(rleft, rright,cleft, cright):
    currcolor=square[rleft][cleft]
    check=0
    for i in range(rleft, rright + 1):
        for j in range(cleft, cright+1):
            if square[i][j]!=currcolor:
                mid = (rleft + rright) // 2
                findsquare(rleft, mid,cleft,mid)
                findsquare(rleft, mid,mid + 1, cright)
                findsquare(mid + 1, rright,cleft,mid)
                findsquare(mid + 1, rright,mid + 1, cright)
                check=1
                return
    if check==0:
        color[currcolor]+=1
num = int(input())
for i in range(num):
    temp = input().split()
    square.append(list(map(int,temp)))
findsquare(0, num - 1,0, num - 1)
print(color[0])
print(color[1])



#white = 0
#blue = 0
#square = []
#def findsquare(left, right):
#    temp = []
#    for i in range(left, right + 1):
#        temp.append(square[i][left:right + 1])
#    if 1 not in temp:
#        white+=1
#    elif 0 not in temp:
#        blue+=1
#    else:
#        mid = (left + right) // 2
#        findsquare(left, mid)
#        findsquare(mid + 1, right)
#num = int(input())
#for i in range(num):
#    temp = input().split()
#    square.append(list(map(int,temp)))
#findsquare(0, num - 1)
#print(white)
#print(blue)
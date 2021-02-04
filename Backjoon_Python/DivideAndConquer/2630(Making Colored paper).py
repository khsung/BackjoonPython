#2630 색종이 만들기
color = [0,0]
square = []
def findsquare(rleft, rright,cleft, cright):  #4개로 구분지어 받아야됨
    temp = []
    wcount = 0
    bcount = 0
    for i in range(left, right + 1):
        temp.append(square[i][left:right + 1])
        wcount+=square[i][left:right + 1].count(0)
        bcount+=square[i][left:right + 1].count(1)
    print(temp)
    if bcount == 0:
        color[0]+=1
    elif wcount == 0:
        color[1]+=1
    else:
        mid = (left + right) // 2
        findsquare(left, mid)
        findsquare(mid + 1, right)
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
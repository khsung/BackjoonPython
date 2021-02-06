#11758 CCW
line=[]
for i in range(3):
    a,b=input().split()
    line.append([int(a),int(b)])
res=(line[0][0]*line[1][1]+line[1][0]*line[2][1]+line[2][0]*line[0][1])-(line[1][0]*line[0][1]+line[2][0]*line[1][1]+line[0][0]*line[2][1])
if res<0:
    print(-1)
elif res==0:
    print(0)
else:
    print(1)
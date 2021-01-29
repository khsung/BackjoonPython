
#1011 Fly me to the Alpha Centauri

num=int(input())
res=[]
for i in range(num):
    count=0
    speed=1
    x,y=input().split(" ")
    distance=int(y)-int(x)
    while distance>0:
        if speed>=distance:
            distance-=speed
            count+=1
        else:
            distance-=2*speed
            count+=2
            speed+=1
    res.append(count)

for i in range(len(res)):
    print(res[i])
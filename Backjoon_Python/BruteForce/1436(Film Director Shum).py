
#1436 Film Director Shum

num=int(input())
count=0
film=666
while count!=num:
    temp=film
    res=temp
    while temp>0:
        if temp%10==6 and (temp//10)%10==6 and ((temp//10)//10)%10==6:
            count+=1
            break
        temp=temp//10
    film+=1
print(res)


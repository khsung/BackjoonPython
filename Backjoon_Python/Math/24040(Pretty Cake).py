#24040 예쁜 케이크
t=int(input())
for i in range(t):
    n=int(input())
    if int(n**0.5)%3==0:
        if (n-(int(n**0.5))**2)==0 or (n-(int(n**0.5))**2)%3==2:
            print('TAK')
        else:
            print('NIE')
    else:
        if (n-(int(n**0.5))**2)%3==1:
            print('TAK')
        else:
            print('NIE')


#1   4
#2   6
#3   8
#4   10,8
#5   12
#6   14,10
#7   16
#8   18,12
#9   20,12
#10  22,14
#11  24
#12  26,16,14
#13  28
#14  30
#15  32,16
#16  34,20,16
#17  36
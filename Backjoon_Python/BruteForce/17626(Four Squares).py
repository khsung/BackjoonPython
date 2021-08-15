#17626 Four Squares
import math
square=[i*i for i in range(224)]
n=int(input())
if n in square:
    print(1)
else:
    check=False
    for i in range(1,int(math.sqrt(n)+1)):
        for j in range(1,int(math.sqrt(n)+1)):
            if square[i]+square[j]==n:
                check=True
                print(2)
                break
        if check:
            break
    if not check:
        for i in range(1,int(math.sqrt(n)+1)):
            for j in range(1,int(math.sqrt(n)+1)):
                if n-(square[i]+square[j]) in square:
                    check=True
                    print(3)
                    break
            if check:
                break
        if not check:
            print(4)
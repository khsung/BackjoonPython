
#셀프 넘버
def checkNum(self, num, boolean):
    if num > 10000:
        return
    elif boolean == True:
        nextnum = num
        while num > 0:
            nextnum+=num % 10
            num = num // 10
        return checkNum(self, nextnum, False)
    else:
        self[num - 1] = False
        nextnum = num
        while num > 0:
            nextnum+=num % 10
            num = num // 10
        return checkNum(self, nextnum, False)

self_num = [True for i in range(10000)]
checkNum(self_num, 1, True)
for i in range(10000):
    if self_num[i] == True:
        checkNum(self_num, i + 1, True)
for i in range(10000):
    if self_num[i] == True:
        print(i + 1)
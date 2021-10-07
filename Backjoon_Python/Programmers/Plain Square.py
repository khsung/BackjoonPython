#멀쩡한 사각형
import math
def find_factor(w,h):
    if h%w==0:
        return w
    else:
        return find_factor(h%w,w)


def solution(w,h):
    answer = 1
    if w>h:
        w,h=h,w
    temp=find_factor(w,h)
    tempw=w//temp
    temph=h//temp
    return w*h-(math.ceil(temph/tempw))*tempw*temp

w=8
h=12
print(solution(w,h))
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
    return w*h-(w+h-temp)

w=10
h=2
print(solution(w,h))
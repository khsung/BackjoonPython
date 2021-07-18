#문자열을 문자 기준으로 나눠서 리스트로 저장
string.split('문자')

#기존 문자열을 대체함
string.replace("기존 문자열","바꿀 문자열")

#숫자의 아스키코드값에 해당하는 문자
chr(숫자)

#문자에 해당하는 아스키코드값
ord(문자)

#공백 기준으로 여러개 입력받기
a,b=input().split(" ")

#리스트에서 최대, 최대인덱스, 최소, 최소인덱스값 찾기
value=[1,2,3,4,5]
max(value), value.index(max(value)), min(value), value.index(min(value))

#리스트 반전
list.reverse()

#num을 문자열로 반환
str(num)

#리스트에서 최댓값, 최소값, 인덱스 반환
max(list), min(list), list.index(a)

#키를 기준으로 정렬하기
sorted(list, key=lambda x:(x[0],x[1]))

#리스트의 개수에 대한 함수 모듈
import collections

#최소힙 모듈
import heapq
heapq.heappush(array, number)
heapq.heappop(array)

#반복제한 설정과 입력받기
import sys
sys.setrecursionlimit(10**6)
sys.stdin.readline()

#얕은 복사와 깊은 복사
import copy
b=copy.copy(a); b=copy.deepcopy(a)

#날짜 원하는 형태 출력
from datetime import datetime
print(datetime.today().strftime("%Y-%m-%d"))

#데크 사용
from collections import deque
deque()     #데크선언
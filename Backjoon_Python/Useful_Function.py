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
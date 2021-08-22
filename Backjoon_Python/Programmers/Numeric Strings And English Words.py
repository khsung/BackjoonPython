#숫자 문자열과 영단어
def solution(s):
    answer = 0
    num_word={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    nums=[i for i in range(10)]
    curr_index=0
    while curr_index<len(s):
        if ord(s[curr_index])-48 in nums:
            answer=10*answer+ord(s[curr_index])-48
            curr_index+=1
        elif s[curr_index:curr_index+3] in num_word:
            answer=10*answer+num_word[s[curr_index:curr_index+3]]
            curr_index+=3
        elif s[curr_index:curr_index+4] in num_word:
            answer=10*answer+num_word[s[curr_index:curr_index+4]]
            curr_index+=4
        else:
            answer=10*answer+num_word[s[curr_index:curr_index+5]]
            curr_index+=5

    return answer

s=["one4seveneight","23four5six7","2three45sixseven","123"]
for i in range(len(s)):
    print(solution(s[i]))
#위장
def solution(clothes):
    answer = 1
    genre={}
    for i in range(len(clothes)):
        if clothes[i][1] not in genre:
            genre[clothes[i][1]]=clothes[i][0]
        else:
            genre[clothes[i][1]]+=" "+clothes[i][0]
    for i in genre.values():
        answer=answer*(len(i.split())+1)
    answer-=1
    return answer

clothes=[[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]],[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]]
for i in range(len(clothes)):
    print(solution(clothes[i]))
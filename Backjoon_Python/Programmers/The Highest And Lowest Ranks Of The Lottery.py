#로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    answer = []
    lotto_rating={6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    zero_cnt=0
    correct=0
    for i in range(6):
        if lottos[i] ==0:
            zero_cnt+=1
        elif lottos[i] in win_nums:
            correct+=1
    answer.append(lotto_rating[correct+zero_cnt])
    answer.append(lotto_rating[correct])
    return answer

lottos=[[44, 1, 0, 0, 31, 25],[0, 0, 0, 0, 0, 0],[45, 4, 35, 20, 3, 9]]
win_nums=[[31, 10, 45, 1, 6, 19],[38, 19, 20, 40, 15, 25],[20, 9, 3, 45, 4, 35]]

for i in range(len(lottos)):
    print(solution(lottos[i], win_nums[i]))
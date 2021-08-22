#키패드 누르기
def solution(numbers, hand):
    answer = ''
    keypad_dic={}
    keypad_dic[1]=[0,0]
    keypad_dic[2]=[0,1]
    keypad_dic[3]=[0,2]
    keypad_dic[4]=[1,0]
    keypad_dic[5]=[1,1]
    keypad_dic[6]=[1,2]
    keypad_dic[7]=[2,0]
    keypad_dic[8]=[2,1]
    keypad_dic[9]=[2,2]
    keypad_dic[0]=[3,1]
    keypad_dic["*"]=[3,0]
    keypad_dic["#"]=[3,2]
    left=[3,0]
    right=[3,2]
    for i in numbers:
        if keypad_dic[i][1]==0:
            answer+="L"
            left=keypad_dic[i]
        elif keypad_dic[i][1]==2:
            answer+="R"
            right=keypad_dic[i]
        else:
            if abs(left[0]-keypad_dic[i][0])+abs(left[1]-keypad_dic[i][1])>abs(right[0]-keypad_dic[i][0])+abs(right[1]-keypad_dic[i][1]):
                answer+="R"
                right=keypad_dic[i]
            elif abs(left[0]-keypad_dic[i][0])+abs(left[1]-keypad_dic[i][1])<abs(right[0]-keypad_dic[i][0])+abs(right[1]-keypad_dic[i][1]):
                answer+="L"
                left=keypad_dic[i]
            else:
                if hand=="left":
                    answer+="L"
                    left=keypad_dic[i]
                else:
                    answer+="R"
                    right=keypad_dic[i]
    return answer

numbers=[[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]
hand=["right","left","right"]
for i in range(len(numbers)):
    print(solution(numbers[i], hand[i]))
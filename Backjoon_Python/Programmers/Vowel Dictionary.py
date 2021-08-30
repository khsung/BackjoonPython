#모음 사전
def solution(word):
    word_dic={}
    curr_value=1
    alpha={0:"A",1:"E",2:"I",3:"O",4:"U"}
    for a in range(5):
        word_dic[alpha[a]]=curr_value
        curr_value+=1
        for b in range(5):
            word_dic[alpha[a]+alpha[b]]=curr_value
            curr_value+=1
            for c in range(5):
                word_dic[alpha[a]+alpha[b]+alpha[c]]=curr_value
                curr_value+=1
                for d in range(5):
                    word_dic[alpha[a]+alpha[b]+alpha[c]+alpha[d]]=curr_value
                    curr_value+=1
                    for e in range(5):
                        word_dic[alpha[a]+alpha[b]+alpha[c]+alpha[d]+alpha[e]]=curr_value
                        curr_value+=1
    answer=word_dic[word]
    return answer

word=["AAAAE","AAAE","I","EIO"]
for i in range(len(word)):
    print(solution(word[i]))

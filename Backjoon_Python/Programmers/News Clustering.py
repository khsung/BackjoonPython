#뉴스 클러스터링
def solution(str1, str2):
    answer = 0
    str1_list=[]
    str2_list=[]
    str1_cnt=str2_cnt=0
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            temp=str1[i].upper()+str1[i+1].upper()
            str1_list.append(temp)
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            temp=str2[i].upper()+str2[i+1].upper()
            str2_list.append(temp)

    if len(str1_list)==0 and len(str2_list)==0:
        answer=65536
    else:
        for i in range(len(str1_list)):
            if str1_list[i] in str2_list:
                str1_cnt+=1
        for i in range(len(str2_list)):
            if str2_list[i] in str1_list:
                str2_cnt+=1
        if str1_cnt<str2_cnt:
            answer=int((str1_cnt*65536)/(len(str1_list)+len(str2_list)-str1_cnt))
        else:
            answer=int((str2_cnt*65536)/(len(str1_list)+len(str2_list)-str2_cnt))

    return answer

str1=["FRANCE","handshake","aa1+aa2","E=M*C^2"]
str2=["french","shake hands","AAAA12","e=m*c^2"]

for i in range(len(str1)):
    print(solution(str1[i], str2[i]))
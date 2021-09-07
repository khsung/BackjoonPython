#뉴스 클러스터링
def solution(str1, str2):
    answer = 0
    inter_cnt=0
    str1_list=[]
    str2_list=[]
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_list.append(str1[i:i+2].lower())
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_list.append(str2[i:i+2].lower())
    visited=[0 for i in range(len(str2))]
    if len(str1_list)==0 and len(str2_list)==0:
        answer=65536
    else:
        for i in range(len(str1_list)):
            for j in range(len(str2_list)):
                if str1_list[i]==str2_list[j] and visited[j]==0:
                    inter_cnt+=1
                    visited[j]=1
                    break
        answer=int((inter_cnt/(len(str1_list)+len(str2_list)-inter_cnt))*65536)
    return answer

str1=["FRANCE","handshake","aa1+aa2","E=M*C^2"]
str2=["french","shake hands","AAAA12","e=m*c^2"]

for i in range(len(str1)):
    print(solution(str1[i], str2[i]))
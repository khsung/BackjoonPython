#직업군 추천하기
def solution(table, languages, preference):
    answer = ''
    max_score=0
    temp_answer=[]
    for i in range(len(table)):
        table[i]=list(table[i].split())
        temp=0
        for j in range(len(languages)):
            try:
                temp+=((6-table[i].index(languages[j]))*preference[j])
            except:
                pass
        if temp>max_score:
            max_score=temp
            temp_answer=[table[i][0]]
        elif temp==max_score:
            temp_answer.append(table[i][0])
    temp_answer.sort()
    answer=temp_answer[0]
    return answer

table=[["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]]
languages=[["PYTHON", "C++", "SQL"],["JAVA", "JAVASCRIPT"]]
preference=[[7, 5, 5],[7, 5]]

for i in range(len(table)):
    print(solution(table[i], languages[i], preference[i]))
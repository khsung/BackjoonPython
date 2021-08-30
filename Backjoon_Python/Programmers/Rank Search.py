#순위 검색
def solution(info, query):
    answer = []
    test_info=[[[[[],[]],[[],[]]],[[[],[]],[[],[]]]],[[[[],[]],[[],[]]],[[[],[]],[[],[]]]],[[[[],[]],[[],[]]],[[[],[]],[[],[]]]]]
    lang={"cpp":0,"java":1,"python":2}
    job={"backend":0,"frontend":1}
    carr={"junior":0,"senior":1}
    food={"chicken":0,"pizza":1}
    for i in range(len(info)):
        info[i]=info[i].split()
        test_info[lang[info[i][0]]][job[info[i][1]]][carr[info[i][2]]][food[info[i][3]]].append(int(info[i][4]))
    
    for i in range(len(query)):
        query[i]=query[i].split(" and ")
        query[i].append(0)
        query[i][3],query[i][4]=query[i][3].split()
        temp_cnt=0
        if query[i][0]=="-":
            lang_cnt=[0,1,2]
        else:
            lang_cnt=[lang[query[i][0]]]
        if query[i][1]=="-":
            job_cnt=[0,1]
        else:
            job_cnt=[job[query[i][1]]]
        if query[i][2]=="-":
            carr_cnt=[0,1]
        else:
            carr_cnt=[carr[query[i][2]]]
        if query[i][3]=="-":
            food_cnt=[0,1]
        else:
            food_cnt=[food[query[i][3]]]
        for a in lang_cnt:
            for b in job_cnt:
                for c in carr_cnt:
                    for d in food_cnt:
                        for e in test_info[a][b][c][d]:
                            if e>=int(query[i][4]):
                                temp_cnt+=1

        answer.append(temp_cnt)

    return answer

info=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))
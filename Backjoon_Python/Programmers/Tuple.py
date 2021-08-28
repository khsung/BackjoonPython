#튜플
def solution(s):
    answer = []
    s=list(s.split("},{"))
    for i in range(len(s)):
        while "{" in s[i] or "}" in s[i]:
            s[i]=s[i].replace("{","").replace("}","")
        s[i]=list(map(int,s[i].split(",")))
    s.sort(key=lambda x:len(x))
    answer.append(s[0][0])
    for i in range(1,len(s)):
        for j in range(len(s[i])):
            if s[i][j] not in answer:
                answer.append(s[i][j])
                break
    return answer

s=["{{2},{2,1},{2,1,3},{2,1,3,4}}","{{1,2,3},{2,1},{1,2,4,3},{2}}","{{20,111},{111}}","{{123}}","{{4,2,3},{3},{2,3,4,1},{2,3}}"]

for i in range(len(s)):
    print(solution(s[i]))
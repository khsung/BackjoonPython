#방금 그곡
def solution(m, musicinfos):
    answer = ''
    play_time=0
    for i in range(len(musicinfos)):
        temp=musicinfos[i].split(",")
        start=list(map(int,temp[0].split(":")))
        end=list(map(int,temp[1].split(":")))
        total=(end[0]-start[0])*60+(end[1]-start[1])
        
        while "#" in temp[3]:
            temp[3]=temp[3].replace(temp[3][temp[3].find("#")-1]+"#",chr(ord(temp[3][temp[3].find("#")-1])+32))
            
        while "#" in m:
            m=m.replace(m[m.find("#")-1]+"#",chr(ord(m[m.find("#")-1])+32))

        temp[3]=temp[3]*(total//len(temp[3]))+temp[3][:total%len(temp[3])]
        if m in temp[3]:
            if play_time<total:
                play_time=total
                answer=temp[2]

    if answer=="":
        answer="(None)"
    return answer

m=["ABCDEFG","CC#BCC#BCC#BCC#B","ABC"]
musicinfos=[["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"],
            ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"],
            ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]]

for i in range(len(m)):
    print(solution(m[i], musicinfos[i]))
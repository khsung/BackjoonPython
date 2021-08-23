#방금 그곡
def solution(m, musicinfos):
    answer = ''
    while "#" in m:
        m=m.replace("C#","c")
        m=m.replace("D#","d")
        m=m.replace("F#","f")
        m=m.replace("G#","g")
        m=m.replace("A#","a")
    for i in range(len(musicinfos)):
        minute=0
        musicinfos[i]=list(musicinfos[i].split(","))
        musicinfos[i][0]=list(map(int,musicinfos[i][0].split(":")))
        musicinfos[i][1]=list(map(int,musicinfos[i][1].split(":")))

        while "#" in musicinfos[i][3]:
            musicinfos[i][3]=musicinfos[i][3].replace("C#","c")
            musicinfos[i][3]=musicinfos[i][3].replace("D#","d")
            musicinfos[i][3]=musicinfos[i][3].replace("F#","f")
            musicinfos[i][3]=musicinfos[i][3].replace("G#","g")
            musicinfos[i][3]=musicinfos[i][3].replace("A#","a")

        if musicinfos[i][0][1]<=musicinfos[i][1][1]:
            minute=musicinfos[i][1][1]-musicinfos[i][0][1]
        else:
            musicinfos[i][0][0]+=1
            minute=60-(musicinfos[i][0][1]-musicinfos[i][1][1])
        minute+=((musicinfos[i][1][0]-musicinfos[i][0][0])*60)
        
        if minute<=len(musicinfos[i][3]):
            musicinfos[i][3]=musicinfos[i][3][:minute]
        else:
            tempa=minute//len(musicinfos[i][3])
            tempb=minute%len(musicinfos[i][3])
            musicinfos[i][3]=musicinfos[i][3]*tempa+musicinfos[i][3][:tempb]
        if m in musicinfos[i][3]:
            answer=musicinfos[i][2]
            break
    if answer=="":
        answer="(None)"
    return answer

m=["ABCDEFG","CC#BCC#BCC#BCC#B","ABC"]
musicinfos=[["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"],
            ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"],
            ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]]

for i in range(len(m)):
    print(solution(m[i], musicinfos[i]))
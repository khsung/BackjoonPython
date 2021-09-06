#파일명 정렬
def solution(files):
    answer = []
    tempanswer=[]
    for i in range(len(files)):
        tempanswer.append([[],[],[]])
        for j in range(len(files[i])):
            if files[i][j].isdigit():
                tempanswer[i][0].append(files[i][:j])
                tempanswer[i][0].append(files[i][:j].lower())
                check=True
                for k in range(5):
                    if j+k>=len(files[i]):
                        break
                    elif not files[i][j+k].isdigit():
                        tempanswer[i][1].append(files[i][j:j+k])
                        tempanswer[i][1].append(int(files[i][j:j+k]))
                        tempanswer[i][2].append(files[i][j+k:])
                        check=False
                        break
                if check:
                    tempanswer[i][1].append(files[i][j:])
                    tempanswer[i][1].append(int(files[i][j:]))
                break
    tempanswer.sort(key=lambda x:(x[0][1],-x[1][1],x[2][0]))
    tempanswer.reverse()
    for i in range(len(tempanswer)):
        temp=(tempanswer[i][0][0]+tempanswer[i][1][0]+tempanswer[i][2][0])
        answer.append(temp)
    return answer

files=[["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"],
        ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]]

for i in range(len(files)):
    print(solution(files[i]))
#파일명 정렬
def solution(files):
    answer = []
    file_list=[[]for i in range(len(files))]
    for i in range(len(files)):
        head=""
        while files[i][0].isalpha() or files[i][0]=="-" or files[i][0]==" ":
            head+=files[i][0]
            files[i]=files[i][1:]
        file_list[i].append(head)
        number=""
        for j in range(5):
            if files[i][0].isdigit():
                number+=files[i][0]
                files[i]=files[i][1:]
            else:
                break
        file_list[i].append(number)
        file_list[i].append(files[i])
    file_list.sort(key=lambda x:(x[0].upper(),int(x[1])))
    for i in range(len(file_list)):
        temp=str(file_list[i][0])+str(file_list[i][1])+str(file_list[i][2])
        answer.append(temp)
    return answer

files=[["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"],
        ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]]

for i in range(len(files)):
    print(solution(files[i]))
#거리두기 확인하기
def solution(places):
    answer = []
    for i in range(len(places)):
        mem_location=[]
        check=1
        for j in range(len(places[i])):
            for k in range(len(places[i][j])):
                if places[i][j][k]=="P":
                    mem_location.append([j,k])
        for j in range(len(mem_location)-1):
            for k in range(j+1,len(mem_location)):
                if abs(mem_location[j][0]-mem_location[k][0])+abs(mem_location[j][1]-mem_location[k][1])==1:
                    check=0
                    break
                elif abs(mem_location[j][0]-mem_location[k][0])+abs(mem_location[j][1]-mem_location[k][1])==2:
                    if mem_location[j][0]==mem_location[k][0]:
                        if places[i][mem_location[j][0]][(mem_location[j][1]+mem_location[k][1])//2]=="O":
                            check=0
                            break
                    elif mem_location[j][1]==mem_location[k][1]:
                        if places[i][(mem_location[j][0]+mem_location[k][0])//2][mem_location[j][1]]=="O":
                            check=0
                            break
                    else:
                        if places[i][mem_location[j][0]][mem_location[k][1]]=="O" or places[i][mem_location[k][0]][mem_location[j][1]]=="O":
                            check=0
                            break
      
        answer.append(check)
    return answer

places=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))

#프렌즈4블록
def solution(m, n, origin_board):
    answer = 0
    bomb_check=[]
    board=[]
    for i in range(len(origin_board)):
        board.append(list(origin_board[i]))
    while True:
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]!=0 and board[i][j]==board[i][j+1] and board[i+1][j]==board[i][j+1] and board[i+1][j]==board[i+1][j+1]:
                    bomb_check.append([i,j])
        
        if len(bomb_check)==0:
            break
        else:
            for  i in bomb_check:
                if board[i[0]][i[1]]!=0:
                    board[i[0]][i[1]]=0
                    answer+=1
                if board[i[0]][i[1]+1]!=0:
                    board[i[0]][i[1]+1]=0
                    answer+=1
                if board[i[0]+1][i[1]]!=0:
                    board[i[0]+1][i[1]]=0
                    answer+=1
                if board[i[0]+1][i[1]+1]!=0:
                    board[i[0]+1][i[1]+1]=0
                    answer+=1

            for i in range(m-1,0,-1):
                for j in range(n):
                    if board[i][j]==0:
                        for k in range(i-1,-1,-1):
                            if board[k][j]!=0:
                                board[i][j],board[k][j]=board[k][j],board[i][j]
                                break
            bomb_check=[]
    return answer


m=[4,6]
n=[5,6]
board=[["CCBDE", "AAADE", "AAABF", "CCBBF"],["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]]

for i in range(len(m)):
    print(solution(m[i], n[i], board[i]))
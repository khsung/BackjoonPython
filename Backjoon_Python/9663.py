def addAtackLine(self, row, column, N):
    for i in range(N):
        self[row][i] += 1
        self[i][column] += 1
    self[row][column] -= 1
    r = row - 1
    c = column + 1
    while r<N and r>=0 and c<N and c>=0:
        self[r][c] += 1
        r -= 1
        c += 1
    r = row + 1
    c = column + 1
    while r<N and r>=0 and c<N and c>=0:
        self[r][c] += 1
        r += 1
        c += 1
    r = row - 1
    c = column - 1
    while r<N and r>=0 and c<N and c>=0:
        self[r][c] += 1
        r -= 1
        c -= 1

    r = row + 1
    c = column - 1
    while r<N and r>=0 and c<N and c>=0:
        self[r][c] += 1
        r += 1
        c -= 1
def delAtackLine(self, row, column, N):
    for i in range(N):
        self[row][i] -= 1
        self[i][column] -= 1
    self[row][column] += 1
    r = row - 1
    c = column + 1
    while r<N and r>=0 and c<N and c>=0:
        self[r][c] -= 1
        r -= 1
        c += 1
    r = row + 1
    c = column + 1
    while r<N and r>=0 and c<N and c>=0:
        self[r][c] -= 1
        r += 1
        c += 1
    r = row - 1
    c = column - 1
    while r<N and r>=0 and c<N and c>=0:
        self[r][c] -= 1
        r -= 1
        c -= 1
    r = row + 1
    c = column - 1
    while r<N and r>=0 and c<N and c>=0:
        self[r][c] -= 1
        r += 1
        c -= 1

def N_Queen(self, row, N):
    global count
    #print("row = ",row)
    #p(self,N)
    if row < N-1:
        for i in range(N):
            if self[row][i] == 0:
                addAtackLine(self, row, i, N)
                N_Queen(self, row+1, N)
                delAtackLine(self, row, i, N)
    else:
        for i in range(N):
            if self[row][i] == 0:
                count+=1
count=0
num=int(input())
chess=[[0]*num for i in range(num)]
N_Queen(chess, 0, num)
print(count)

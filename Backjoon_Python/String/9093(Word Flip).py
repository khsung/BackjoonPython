#9093 단어 뒤집기
n=int(input())
for i in range(n):
    string=list(input().split())
    for j in range(len(string)):
        print(string[j][::-1],end=" ")
    print()
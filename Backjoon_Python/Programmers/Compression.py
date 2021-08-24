#압축
def solution(msg):
    answer = []
    alpha={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
    last_value=27
    curr_index=0
    while curr_index<len(msg):
        distance=2
        while msg[curr_index:curr_index+distance] in alpha and curr_index+distance-1<=len(msg):
            distance+=1
        answer.append(alpha[msg[curr_index:curr_index+distance-1]])
        alpha[msg[curr_index:curr_index+distance]]=last_value
        last_value+=1
        curr_index=curr_index+distance-1
    return answer


msg=["KAKAO","TOBEORNOTTOBEORTOBEORNOT","ABABABABABABABAB"]
for i in range(len(msg)):
    print(solution(msg[i]))
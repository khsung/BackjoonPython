#신규 아이디 추천
def solution(new_id):
    answer = ''
    new_id=new_id.lower()
    temp_ans=""
    for i in new_id:
        if 97<=ord(i)<=122 or 45<=ord(i)<=46 or ord(i)==48 or ord(i)==57 or ord(i)==95 or 48<=ord(i)<=57:
            temp_ans+=i
    while ".." in temp_ans:
        temp_ans=temp_ans.replace("..",".")
    if len(temp_ans)>0 and temp_ans[0]==".":
        temp_ans=temp_ans[1:]
    if len(temp_ans)>0 and temp_ans[len(temp_ans)-1]==".":
        temp_ans=temp_ans[:-1]

    if len(temp_ans)==0:
        temp_ans+="a"

    if len(temp_ans)>=16:
        temp_ans=temp_ans[:15]
        if temp_ans[14]==".":
            temp_ans=temp_ans[:14]

    while len(temp_ans)<=2:
        temp_ans+=temp_ans[len(temp_ans)-1]

    answer=temp_ans
    return answer

new_id=["...!@BaT#*..y.abcdefghijklm","z-+.^.","=.=","123_.def","abcdefghijklmn.p"]
for i in range(len(new_id)):
    print(solution(new_id[i]))

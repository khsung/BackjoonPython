#스킬 트리
def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        curr=0
        check=True
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j]==skill[curr]:
                curr+=1
                if curr>=len(skill):
                    break
            elif skill_trees[i][j] in skill and skill_trees[i][j] not in skill[:curr+1]:
                check=False

        if check:
            answer+=1

    return answer

skill="CBD"
skill_trees=["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))
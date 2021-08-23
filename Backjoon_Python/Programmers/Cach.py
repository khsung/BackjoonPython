#캐시
def solution(cacheSize, cities):
    answer = 0
    queue=[]
    if cacheSize==0:
        answer=len(cities)*5
    else:
        for i in cities:
            i=i.lower()
            if len(queue)<cacheSize:
                if i not in queue:
                    queue.append(i)
                    answer+=5
                else:
                    queue.remove(i)
                    queue.append(i)
                    answer+=1
            else:
                if i not in queue:
                    queue.pop(0)
                    queue.append(i)
                    answer+=5
                else:
                    queue.remove(i)
                    queue.append(i)
                    answer+=1
    return answer

cacheSize=[3,3,2,5,2,0]
cities=[["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", 
         "LA"],["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", 
         "Seoul"],["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", 
         "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"],["Jeju", "Pangyo", "Seoul", 
         "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"],
         ["Jeju", "Pangyo", "NewYork", "newyork"],["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]]

for i in range(len(cities)):
    print(solution(cacheSize[i], cities[i]))
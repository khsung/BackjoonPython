#힙 선언과 사용법
import heapq
data_list=[]
input_data=[5,9,3,1]
print("최소 힙 초기 원소 :",data_list)
for i in input_data:
    print(i,"추가")
    heapq.heappush(data_list,i)
    print(data_list)

print("\n최소 힙 루트 노드의 원소 :",data_list[0],end="\n\n")

for i in range(len(input_data)):
    print(heapq.heappop(data_list),"삭제")
    print(data_list)

print("\n기존 input 리스트 :",input_data)
heapq.heapify(input_data)
print("Heapify 후 input 리스트 :",input_data)

print("\n최대 힙 초기 원소 :",data_list)
for i in input_data:
    print(i,"추가")
    heapq.heappush(data_list,(-i,i))
    print(data_list)

print("\n최대 힙 루트 노드의 원소 :",data_list[0][1],end="\n\n")

for i in range(len(input_data)):
    print(heapq.heappop(data_list)[1],"삭제")
    print(data_list)
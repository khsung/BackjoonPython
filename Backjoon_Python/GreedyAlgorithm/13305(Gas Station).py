#13305 주유소
station_num = int(input())
path = input().split()
path = list(map(int,path))
station = input().split()
station = list(map(int,station))
station.pop()
end = len(station) - 1
costsum = 0
path_sum = 0
mincost = min(station)
mincostindex = station.index(mincost)
for i in range(mincostindex,len(station)):
    path_sum+=path[i]
costsum+=mincost * path_sum
for i in range(mincostindex):
    if i == 0:
        temp = station[i]
    if temp > station[i + 1]:
        costsum=costsum+(temp * path[i])
        temp = station[i + 1]
    else:
        costsum=costsum+(temp * path[i])
print(costsum)
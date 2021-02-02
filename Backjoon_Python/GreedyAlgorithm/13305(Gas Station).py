#13305 주유소
station_num = int(input())
path = input().split()
path = list(map(int,path))
station = input().split()
station = list(map(int,station))
station.pop()
right = len(station) - 1
costsum = 0
while right > -1:
    path_sum = 0
    mincost = min(station)
    mincostindex = station.index(mincost)
    for i in range(mincostindex,right + 1):
        path_sum+=path[i]
    costsum+=path_sum * mincost
    station = station[:mincostindex]
    right = mincostindex - 1
print(costsum)
# https://www.acmicpc.net/problem/17471
# 1. 서로 참고하고있는 그래프를 생성한다.
# 2. 1~N개의 구역까지 모두 dfs 하면서 나눌수있는 구역을 구한뒤, 인구수의 차이의 최소값을 갱신한다.

# N번에서 (1개, N-1) 그룹까지 모든 구역리스트 구한다.
# 나머지 그룹이 가능한 리스트들을 구한다
# 최소거리를 구한뒤 
from copy import deepcopy
N = int(input())
people = [0] + list(map(int, input().split()))
graph = [set() for _ in range(N+1)]
distance = [0 for _ in range((1<<N) - 1)] # 모든 경우의 수를 거리를 구한다.

for i in range(1, N+1):
    cityinfo = list(map(int ,input().split()))
    for j in range(1, len(cityinfo)):
        graph[i].add(cityinfo[j])
        graph[cityinfo[j]].add(i)
        
def dfs(city, citylist, depth, mycitylist):
    if len(citylist) >= depth: # depth 까지 도착했으면 CityList들의 후보에 추가
        mycitylist.append(deepcopy(citylist))
        return
    
    for newcity in graph[city]:
        if newcity not in citylist:
            citylist.append(newcity)
            dfs(newcity, citylist, depth)
            citylist.pop()

mycitylist = []
for i in range(1, N+1):
    for j in range(1, N):
        citylist = []
        citylist.append(i)
        dfs(i, citylist, j)
        citylist.pop()

mycitylist2 = []
for citylist in mycitylist:
    for i in range(1, N+1):
        if i not in citylist:
            dfs(i, )
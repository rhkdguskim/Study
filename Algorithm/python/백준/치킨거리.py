# https://www.acmicpc.net/problem/15686
import sys
from itertools import combinations
INF = int(1e9)

input = sys.stdin.readline

N , M = map(int, input().split())

chicken = []
house = []

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 1:
            house.append((i+1, j+1))
        elif temp[j] == 2:
            chicken.append((i+1, j+1))

ans = INF
for chicken_com in combinations(chicken, M): # 치킨 조합을 구한다.
    distance = [INF for _ in range(len(house))] # 거리의 값을 최대값으로 초기화 시킨다.
    for i in range(len(house)):
        for chick in chicken_com:
            # 치킨 거리값이 가장 짧은 값을 찾는다.
            distance[i] = min(distance[i], abs(house[i][0] - chick[0]) + abs(house[i][1] - chick[1]))
    
    ans = min(sum(distance), ans) # 제일 작은 치킨 거리값을 찾는다.
    
print(ans)
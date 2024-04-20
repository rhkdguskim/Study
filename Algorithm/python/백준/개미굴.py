# https://www.acmicpc.net/problem/14725
# 입력받은 데이터값을 정렬한다. ( 알파벳순이 빠른순으로 )
# 배열을 순회하면서 방문한 흔적을 남긴다.
# 이미 방문한 흔적과 같은 루트를 탔다면 무시한다.

import sys
input = sys.stdin.readline

visited = set()

N = int(input())
ants_route = []
for _ in range(N):
    temp = list(map(str, input().split()))
    ants_route.append(temp[1:])

ants_route.sort()


for routes in ants_route:
    path_route = ''
    for i, route in enumerate(routes):
        path_route += route
        if not path_route in visited:
            visited.add(path_route)
            print('--'* i +route)
            
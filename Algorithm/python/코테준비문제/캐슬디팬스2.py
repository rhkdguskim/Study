# https://www.acmicpc.net/problem/17135
import sys
from collections import deque
from copy import deepcopy
moves = [(-1,0), (0,-1), (0, 1)]
input = sys.stdin.readline

N, M, D = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
arrows = [(N, j) for j in range(M)] # 궁수의 위치

# 1. 모든 궁수는 동시에 공격한다. 그리고 적을 구한다.
# 궁수 한명이 적을 공격할 수 있는 적을 return
def attack(arrow, graph):
    visit = [[False for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append((arrow[0], arrow[1]))
    e = [] # 적을 담을 배열
    while queue:
        i, j = queue.popleft()
        for dy, dx in moves:
            ny, nx = i+dy, j+dx
            distacne = abs(arrow[0] - ny) + abs(arrow[1] - nx)
            if N > ny >= 0 and M > nx >= 0 and not visit[ny][nx] and D >= distacne:
                visit[ny][nx] = True
                if e: # 적이 있을경우
                    if distacne > e[0][2]: # 거리가 이미 넘었을경우는 탐색하지 않는다. ( 이미 최단경로임으로 )
                        continue

                queue.append((ny, nx))

                if graph[ny][nx] == 0:
                    continue

                # 적이있고 거리도 최소값의 적만 넣는다.
                e.append((ny, nx, distacne))
    if e: # 적이 있다면
        e.sort(key = lambda x : x[1]) # 가장 왼쪽에 있는 적을 찾는다.
        return e[0]
    else:
        return None

 # 적을 사살한다.
def remove(e, graph):
    cnt = 0
    for i, j in e:
        graph[i][j] = 0
        cnt += 1

    return cnt

# 적은 아래로 내려온다.
def down(graph):
    for i in range(N-2, -1, -1):
        graph[i+1] = deepcopy(graph[i])

    graph[0] = [0 for _ in range(M)]

def is_end(graph):
    for i in range(N-1):
        for j in range(M):
            if graph[i][j] == 1: # 적이 있다면 게임이 끝나지 않음
                return False

    return True

ans = 0
arrowcnt = 0
def solve(idx, queue, graph):
    global ans, arrowcnt
    if len(queue) == 3: # 3명의 궁수룰 뽑았으니 이제,,, 게임시작
        arrowcnt += 1
        graph = deepcopy(graph)
        cnt = 0
        while True:
            e = set() # 중복되지 않게 만든다.
            # 궁수가 공격할 적을 구한다.
            for ar in queue:
                temp = attack(ar, graph)
                if temp is not None:
                    e.add((temp[0], temp[1]))

            cnt += len(e) # 몇명의 적을 사살했는지 업데이트
            remove(e, graph)

            # 모든 적이 다 사살되었거나, 적을 다 사살하지 못했을경우.
            if is_end(graph):
                break

            # 적을 아래로 움직인다.
            down(graph)
        # 적의 최대 개수를 업데이트한다.
        ans = max(ans, cnt)
        return

    # 궁수의 조합을 구한다.
    for i in range(idx, len(arrows)):
        queue.append(arrows[i])
        solve(i + 1, queue, graph)
        queue.pop()

solve(0, [], graph)
print(ans)
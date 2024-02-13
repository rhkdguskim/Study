# https://www.acmicpc.net/problem/17471
# 1. A구역 ,B 구역 으로 나눌 수 있는 경우의 수를 모두구한다.
# 2. A구역, B구역으로 각각 잘 나누어 졌는지 확인해야한다.
# 3. 확인하는 방법은 A구역을 확인한다고하면 A구역의 아무 점이나 선택하여 깊이우선탐색을 하였을때, 방문길이가 반드시 구역의 크기 만큼 있어야한다.
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
people = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    temp = list(map(int, input().split()))
    if temp[0] > 0: # 간선의 개수가 0 이상일 경우
        for n in temp[1:]:
            graph[i].append(n)


def is_team(team):
    queue = deque()
    queue.append(team[0])
    visit = [False for _ in range(N+1)]
    for k in range(N+1):
        if k not in team:
            visit[k] = True
    visit[team[0]] = True

    while queue:
        new_n = queue.popleft()
        for new_n2 in graph[new_n]:
            if new_n2 in team and not visit[new_n2]:
                visit[new_n2] = True
                queue.append(new_n2)

    if all(visit):
        return True
    else:
        return False

ans = sum(people)

def people_diff(team, team2):
    temp = 0
    temp2 = 0
    for n in team:
        temp += people[n]
    for n in team2:
        temp2 += people[n]

    return abs(temp - temp2)

def make_team(idx, team):
    global ans
    if team and team[0] > N // 2:
        return

    if N > len(team) > 0: # 모든 팀이 결성이 되면
        team2 = [i for i in range(1, N+1) if i not in team]
        if is_team(team) and is_team(team2):
            #print(team, team2)
            ans = min(people_diff(team, team2), ans)
            #print(ans)

    for n in range(idx, N + 1):
        if n not in team:
            team.append(n)
            make_team(idx + 1,team)
            team.pop()


make_team(1, [])
if ans == sum(people):
    print(-1)
else:
    print(ans)
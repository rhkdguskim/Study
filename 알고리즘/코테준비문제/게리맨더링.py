# https://www.acmicpc.net/problem/17471
from itertools import combinations

N = int(input())
city = {num for num in range(1, N + 1)}
people = [0] + list(map(int, input().split()))  # N+1개의 배열을 생성

graph = [[] for _ in range(N + 1)]  # N+1개의 배열을 생성

for i in range(1, N + 1):
    temp = list(map(int, input().split()))
    for num in temp[1:]:
        graph[i].append(num)
        graph[num].append(i)


def dfs(node, type):# 방문가능한 노드만 방문한다.
    for new in graph[node]:
        if not visited[new] and new in type:
            visited[new] = True
            dfs(new, type)


def check():# 방문하지 못한 도시가 있다면 게리맨더링이 되지 못한다.
    for i in range(1, N + 1):
        if not visited[i]:
            return False

    return True


def sumpeople(blue, red):
    temp1 = 0
    temp2 = 0
    for p in blue:
        temp1 += people[p]
    for p in red:
        temp2 += people[p]

    return abs(temp1 - temp2)


ans = 100 * 100
for i in range(1, (N // 2) + 1):  # 1개의 도시부터 N-1 도시까지 blue 진형의 조합을 구한다.
    combi = combinations(city, i)
    for temp in combi:
        blue = set(temp)
        red = city - blue
        #print(blue, red)
        visited = [False for _ in range(N + 1)]
        for t in blue:
            visited[t] = True
            dfs(t, blue)
            break

        for t in red:
            visited[t] = True
            dfs(t, red)
            break

        if check():

            #print("성공")
            res = sumpeople(blue, red)
            #print(blue, red, res, visited)
            ans = min(res, ans)
        else:
            pass
            #print(visited)
            #print("실패")

if ans == 100 * 100:
    print(-1)
else:
    print(ans)

#print(graph)

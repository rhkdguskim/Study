# https://www.acmicpc.net/problem/14890
N, L = map(int, input().split())

table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

moves = [(0, 1), (1, 0)]

# count는 현재 같은 숫자가 얼마나 나왔는지 카운트한다.
def xdfs(i,j):
    prev = table[i][j]
    j += 1
    while N > j:
        cur = table[i][j]
        if prev != cur: # 값이 다르다면
            if abs(prev - cur) > 1:
                return 0

            counter = 0
            if cur > prev: # 현재 값이 이전값보다 크다면 이전에 있던 높이를 확인해본다.
                for t in range(j-1, -1, -1):
                    temp = table[i][t]
                    if prev == temp and not visited[t]:
                        visited[t] = True
                        counter += 1
                        if counter >= L:
                            break
                    else:
                        break
            else: # 현재값이 이전값보다 작다면 이후에 나올 높이를 확인해본다.
                for t in range(j, N):
                    temp = table[i][t]
                    if cur == temp and not visited[t]:
                        visited[t] = True
                        counter += 1
                        j = t
                        if counter >= L:
                            break
                    else:
                        break

            if counter < L:
                return 0

        j += 1
        prev = cur

    return 1

def ydfs(i,j):
    prev = table[i][j]
    i += 1
    while N > i:
        cur = table[i][j]
        if prev != cur: # 값이 다르다면
            if abs(prev - cur) > 1:
                return 0

            counter = 0
            if cur > prev: # 현재 값이 이전값보다 크다면 이전에 있던 높이를 확인해본다.
                for t in range(i-1, -1, -1):
                    temp = table[t][j]
                    if prev == temp and not visited[t]:
                        visited[t] = True
                        counter += 1
                        if counter >= L:
                            break
                    else:
                        break
            else: # 현재값이 이전값보다 작다면 이후에 나올 높이를 확인해본다.
                for t in range(i, N):
                    temp = table[t][j]
                    if cur == temp and not visited[t]:
                        visited[t] = True
                        counter += 1
                        i = t
                        if counter >= L:
                            break
                    else:
                        break

            if counter < L:
                return 0

        i += 1
        prev = cur

    return 1

answer = 0
for i in range(N):
    visited = [False for _ in range(N)]
    ans = xdfs(i, 0)  # y축
    #print("x축", i, 0, ans, visited)

    answer += ans

for i in range(N):
    visited = [False for _ in range(N)]
    ans = ydfs(0, i)  # y축
    #print("y축", 0, i, ans, visited)
    answer += ans

print(answer)

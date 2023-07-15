# 여행을 떠난 세준이는 지도를 하나 구하였다. 이 지도는 아래 그림과 같이 직사각형 모양이며 여러칸으로 나뉘어져있다.
# 한 칸은 한 지점을 나타내는데 각 칸에는 그 지점의 높이가 쓰여있으며, 각 지점 사이의 이동은 지도 상하좌우 이웃한곳 끼리만 가능하다.
# 이동은 가능한 힘을 적게들이고 싶어 더 낮은 지점으로만 이동가능하다.
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 상하좌우 이동

M, N = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]  # 동적 계획법을 위한 메모이제이션 배열

def dfs(i, j): # 깊이우선탐색
    if i == M-1 and j == N-1:  # 목표 지점에 도달하면 1을 반환
        return 1

    if dp[i][j] != -1:  # 이미 계산한 값이 있으면 그 값을 반환
        return dp[i][j]

    dp[i][j] = 0  # 현재 위치에서 가능한 경로의 수를 저장할 변수

    for dx, dy in move:
        nx, ny = i + dx, j + dy

        if 0 <= nx < M and 0 <= ny < N and table[nx][ny] < table[i][j]:
            dp[i][j] += dfs(nx, ny)  # 내리막길로 이동할 수 있는 경우 경로의 수 누적

    return dp[i][j]

result = dfs(0, 0)
print(result)
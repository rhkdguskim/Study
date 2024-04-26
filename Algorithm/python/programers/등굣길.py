# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    div = 1000000007
    # 오른쪽, 아래
    moves = [(0, 1), (1, 0)]
    dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
    puddles = {(j, i) for i, j in puddles}
    dp[n][m] = 1

    def dfs(i, j):
        # 집에 도달하였을때
        if i == n and j == m:
            return dp[n][m]

        # 이미 가는 방법이 계산된경우 또 방문하지 않고 결과를 리턴한다.
        if dp[i][j] != -1:
            return dp[i][j]

        dp[i][j] = 0
        for dy, dx in moves:
            ny, nx = dy + i, dx + j
            # 범위안에 있고, 물웅덩이가 없다면
            if 1 <= ny <= n and 1 <= nx <= m and (ny, nx) not in puddles:
                dp[i][j] += dfs(ny, nx)

        return dp[i][j] % div

    return dfs(1, 1)



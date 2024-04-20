import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

N = int(input())

# 열, 주 대각선, 부 대각선 체크 배열 초기화
column = [False] * N
diag1 = [False] * (2*N - 1)  # row - col
diag2 = [False] * (2*N - 1)  # row + col

def dfs(row):
    if row == N:  # 모든 행에 퀸을 놓았을 경우
        return 1

    total = 0
    for col in range(N):
        if column[col] or diag1[row - col + N - 1] or diag2[row + col]:
            continue

        # 퀸 놓기
        column[col] = diag1[row - col + N - 1] = diag2[row + col] = True
        total += dfs(row + 1)
        # 퀸 제거
        column[col] = diag1[row - col + N - 1] = diag2[row + col] = False

    return total

print(dfs(0))
# https://school.programmers.co.kr/learn/courses/30/lessons/49191

# 플로이드 워셜 알고리즘으로 한 선수가 모든 선수와 연결이 되어 있다면 그 선수는 순위를 알 수 있다.

def solution(n, results):
    visited = [[False]*(n+1) for _ in range(n+1)]

    for a, b in results:
        visited[b][a] = True

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if visited[i][k] and visited[k][j]:
                    visited[i][j] = True

    answer = 0
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if visited[i][j] or visited[j][i]:
                cnt += 1

        if cnt == n-1:
            answer += 1

    return answer
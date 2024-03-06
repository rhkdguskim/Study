# https://www.acmicpc.net/problem/1029
# i번째사람을 선택한경우 선택하지 않은경우로 나눈다.
# i번째사람에 j번째 사람에게 그림을 팔았을때의 최대 수 dp[i][j]
import sys
input = sys.stdin.readline

N = int(input())
edge = [[] for _ in range(N+1)]

for i in range(N):
    temp = list(str(input().strip()))
    for j in range(len(temp)):
        if i != j:
            edge[i+1].append((j+1, int(temp[j])))

stack = [(j, cost, 1) for j, cost in edge[1]]

    
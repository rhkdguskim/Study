# 문제 : https://www.acmicpc.net/problem/14502

# 1. 2로 탐색을 시작하여 벽을 생성한다. ( 무한반복 )
# 2. 등록된 후보로 벽을 생성하여

N , M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

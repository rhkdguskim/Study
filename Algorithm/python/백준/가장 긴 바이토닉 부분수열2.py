# https://www.acmicpc.net/problem/11054

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 증가하는 부분 수열의 길이 계산
increase = [1 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            increase[i] = max(increase[i], increase[j] + 1)

# 감소하는 부분 수열의 길이 계산
decrease = [1 for _ in range(N)]
A = A[::-1]
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

# 바이토닉 수열의 최대 길이 계산
max_length = 0
for i in range(N):
    max_length = max(max_length, increase[i] + decrease[N-i-1] - 1)

# 결과 출력
print(max_length)
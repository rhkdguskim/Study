#https://www.acmicpc.net/problem/1300
# 이분탐색으로 문제를 해결.
# 현재 찾고자하는 값 10000 이라면 10000 보다 작은값을 카운팅하여 카운트 값이 크다면 이분탐색 범위 크기를 낮추고, 카운트값이 작다면 이분탐색 범위를 크게한다.
# 즉 현재 찾고자하는 값을 모두 카운트 해보아 이분탐색한다.

import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

start = 1
end = k
ansnwer = 0
while start <= end:
    mid = (start+end) // 2
    count = 0
    for i in range(1, N+1):
        count += min(mid//i, N)

    if count >= k:
        ansnwer = mid
        end = mid-1
    else:
        start = mid+1

print(ansnwer)
    
    
    
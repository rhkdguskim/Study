# https://www.acmicpc.net/problem/1655
# 큐를 2개로 문제를 해결한다.
# 왼쪽 오른쪽 한번씩 번갈아가면서 큐를 추가한다.
import heapq
import sys
leftq = []
rightq = []
N = int(input())

for _ in range(N):
    num = int(sys.stdin.readline())
    
    if len(leftq) != len(rightq):
        heapq.heappush(rightq, num)
    else:
        heapq.heappush(leftq, -num)
    
    if rightq and rightq[0] < -leftq[0]:
        rightnum = heapq.heappop(rightq)
        leftnum = heapq.heappop(leftq)
        heapq.heappush(rightq, -leftnum)
        heapq.heappush(leftq, -rightnum)
    
    print(-leftq[0])

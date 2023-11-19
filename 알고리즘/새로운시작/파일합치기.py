# https://www.acmicpc.net/problem/11066
import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    queue = list(map(int, input().split()))
    heapq.heapify(queue)
    ans = 0
    while len(queue) != 1:
        file1 = heapq.heappop(queue)
        file2 = heapq.heappop(queue)
        cost = file1 + file2
        ans += cost
        print(ans)
        heapq.heappush(queue, cost)
        
    print(ans)
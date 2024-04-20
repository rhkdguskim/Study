# https://www.acmicpc.net/problem/2075
# N^2 인 시간복잡도로 문제를 해결해야함.
from pprint import pprint
import heapq
import sys
input = sys.stdin.readline
N = int(input())
queue = []

for i in range(N):
    temp = list(map(int, input().split()))
    if i == 0:
        for num in temp:
            heapq.heappush(queue, num)
    else:
        for num in temp:
            if num > queue[0]:
                heapq.heappush(queue, num)
                heapq.heappop(queue)


print(queue[0])
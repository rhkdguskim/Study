# https://www.acmicpc.net/problem/13975
import sys
import heapq

input = sys.stdin.readline


T = int(input())


for _ in range(T):
    K = int(input())
    queue = []
    for file in list(map(int, input().split())):
        heapq.heappush(queue, file)
        
    cost = 0
    while len(queue) != 1:
        file1 = heapq.heappop(queue)
        file2 = heapq.heappop(queue)
        new_file = file1 + file2
        cost += new_file
        heapq.heappush(queue, new_file)
    
    print(cost)
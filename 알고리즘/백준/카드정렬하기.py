# https://www.acmicpc.net/problem/1715
import heapq
import sys
input = sys.stdin.readline

N = int(input())

card = []
for _ in range(N):
    heapq.heappush(card, int(input()))
    

ans = 0

while len(card) != 1:
    card1 = heapq.heappop(card)
    card2 = heapq.heappop(card)
    
    cost = card1+card2
    ans += cost
    heapq.heappush(card, cost)
    
print(ans)
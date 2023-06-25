# https://www.acmicpc.net/problem/1202

# 1) 가방을 제일 작은순으로 정렬한다.
# 2) 가방을 작은순으로 선택한다.
# 3) 무게가 가방의 무게보다 작거나 같으면서 가장 가치있는 아이템을 찾아서 가방에 넣는다.
import heapq
import sys
input = sys.stdin.readline
N, K = map(int, input().split())

item = []
bags = []

for _ in range(N):
    m, v = map(int, input().split()) 
    heapq.heappush(item, [m, v]) # 아이템을 무게가 작은순으로 정렬하여 삽입한다.
    
for _ in range(K):
    m = int(input())
    bags.append(m) # 가방을 무게가 작은순으로 정렬하여 삽입한다.

bags.sort()
result = 0
maxitems = []
for bag in bags: # 30만
    while item and bag >=item[0][0]:
        m, v = heapq.heappop(item)
        heapq.heappush(maxitems, -v)
        
    if maxitems:
        value = heapq.heappop(maxitems)
        result += -value
                    
print(result)
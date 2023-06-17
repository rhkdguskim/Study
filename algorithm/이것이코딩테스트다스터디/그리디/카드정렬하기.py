#https://www.acmicpc.net/problem/1715
import heapq
N = int(input()) # 묶음 카드의 수
queue = []

for _ in range(N):
    heapq.heappush(queue, int(input()))

result = 0
if(N > 1):
    while queue:
        card1 = heapq.heappop(queue)
        card2 = heapq.heappop(queue)
        
        result += card1 + card2
        if not queue: # 큐가 모두 비었다면 결과를 출력한다.
            break
        else :
            heapq.heappush(queue, card1 + card2)
else :
    result = 0

print(result)

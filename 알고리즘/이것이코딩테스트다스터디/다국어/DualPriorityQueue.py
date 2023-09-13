#https://www.acmicpc.net/problem/7662
# 큐에서 딜리트할때 높은우선순위와 혹은 작은우선순위가 함께 지워진다.
# 두개의 명령어가 있다.
# 하나는 인서트하는것이고, 다른하나는 아이템을 지우는것이다.
# 지우는데에는 2개의 파라미터를 갖는다. 높은우선순위를 지우는것(숫자가 높다), 낮은우선순위(숫자가 낮다)를 지운는것
# 1은 우선순위가 높은값을 지우고, -1은 우선순위가 낮은 값을 지운다.

# 우선순위큐 (?)이분탐색으로 가능할듯?

# 테스트케이스T, K는 명령어수(1000000), 그다음에는 명령어가 주어진다.
import heapq

T = int(input())
for _ in range(T):
    k = int(input())
    minq = []
    maxq = []
    visited = [False] * k
    for i in range(k):
        op , temp = map(str, input().split())
        number = int(temp)
        if op == "I":
            heapq.heappush(minq, [number, i])
            heapq.heappush(maxq, [-number, i])
            visited[i] = True
        else:
            if number == 1: # 큰값을 제거하라
                while maxq and not visited[maxq[0][1]]:
                    heapq.heappop(maxq)
                    
                if maxq:
                    visited[maxq[0][1]] = False
                    heapq.heappop(maxq)
            else:
                while minq and not visited[minq[0][1]]:
                    heapq.heappop(minq)
                    
                if minq:
                    visited[minq[0][1]] = False
                    heapq.heappop(minq)
                    
    while minq and not visited[minq[0][1]]:
        heapq.heappop(minq)
        
    while maxq and not visited[maxq[0][1]]:
        heapq.heappop(maxq)
        
    if minq and maxq:
        print(-maxq[0][0], minq[0][0])
    else:
        print("EMPTY")
        
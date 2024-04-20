# https://www.acmicpc.net/problem/7662
import sys
import heapq
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    k = int(input())
    leftq = []
    rightq = []
    for _ in range(k):
        op, payload = map(str, input().split())
        if op == 'I':
            cost = int(payload)
            if cost > 0:
                heapq.heappush(leftq, cost)
                heapq.heappush(rightq, -cost)
            else:
                heapq.heappush(leftq, cost)
                heapq.heappush(rightq, -cost)
        else:
            if payload == "-1":
                if not leftq:
                    heapq.heappop(rightq)
                else:
                    heapq.heappop(leftq)
            else:
                if not rightq:
                    heapq.heappop(leftq)
                else:
                    heapq.heappop(rightq)

        if leftq and rightq:
            while leftq[0] > -rightq[0]:
                num = heapq.heappop(leftq)
                num2 = heapq.heappop(rightq)
                heapq.heappush(leftq,dddd )


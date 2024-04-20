# https://www.acmicpc.net/problem/2696
import sys
import heapq
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    H = (N-1) // 10
    leftq = []
    rightq = []
    result = []
    temp = []
    for _ in range(H+1):
        temp += list(map(int, input().split()))

    cnt = 1  # 홀수 짝수 체크 cnt
    for num in temp:
        if len(leftq) == len(rightq):
            heapq.heappush(leftq, -num)
        else:
            heapq.heappush(rightq, num)

        if rightq and -leftq[0] > rightq[0]:
            num1 = heapq.heappop(leftq)
            num2 = heapq.heappop(rightq)
            heapq.heappush(leftq, -num2)
            heapq.heappush(rightq, -num1)

        if cnt % 2 == 1: # 홀수일때
            result.append(-leftq[0])
        cnt +=1

    print(len(result))
    cnt = 1
    for num in result:
        print(num, end=' ')
        if cnt % 10 == 0:
            print()
        cnt += 1


    if cnt % 10 != 0:
        print()


#https://www.acmicpc.net/problem/7662
# 큐에서 딜리트할때 높은우선순위와 혹은 작은우선순위가 함께 지워진다.
# 두개의 명령어가 있다.
# 하나는 인서트하는것이고, 다른하나는 아이템을 지우는것이다.
# 지우는데에는 2개의 파라미터를 갖는다. 높은우선순위를 지우는것(숫자가 높다), 낮은우선순위(숫자가 낮다)를 지운는것
# 1은 우선순위가 높은값을 지우고, -1은 우선순위가 낮은 값을 지운다.

# 우선순위큐 (?)이분탐색으로 가능할듯?

# 테스트케이스T, K는 명령어수(1000000), 그다음에는 명령어가 주어진다.
from collections import deque


T = int(input())
for _ in range(T):
    k = int(input())
    queue = deque()
    minqueue = deque()
    maxqueue = deque()
    
    for _ in range(k):
        cmd , num = map(str, input().split())
        number = int(num)
        if cmd == 'I': # 삽입
            if minqueue:
                if minqueue[0] >= number:
                    minqueue.appendleft(number)
                else:
                    if maxqueue:
                        if number >= maxqueue[-1]:
                            maxqueue.append(number)
                    else:
                        maxqueue.append(number)  
            elif maxqueue:
                if number >= maxqueue[-1]:
                    maxqueue.append(number)
                else:
                    if minqueue:
                        if minqueue[0] >= number:
                            minqueue.appendleft(number)
                    else:
                        minqueue.appendleft(number)
            else:
                minqueue.append(number)
                maxqueue.append(number)
            
        else:# 삭제
            if number == 1: # 우선순위가 높은 값을 지운다.(숫자가크다)
                if maxqueue:
                    maxqueue.pop()
                else:
                    if minqueue:
                        minqueue.pop()
            else: # 우선순위가 낮은 값을 지운다. (숫자가작다)
                if minqueue:
                    minqueue.popleft()
                else:
                    if maxqueue:
                        maxqueue.popleft()

    queue = list(minqueue + maxqueue)
    queue.sort()
    if queue:
        print(queue[-1], queue[0])
    else:
        print("EMPTY")

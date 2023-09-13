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
        if cmd == 'I': # 큐에 삽입
            if minqueue and minqueue[0] >= number:
                minqueue.append(number)
            elif maxqueue and number >= maxqueue[0]:
                maxqueue.appendleft(number)
            else:
                if not minqueue:
                    minqueue.append(number)
                elif not maxqueue:
                    maxqueue.append(number)
                else:
                    if number > minqueue[0]:
                        while number > maxqueue[-1]:
                            movenum = maxqueue.pop()
                            minqueue.appendleft(movenum)
                        
                        maxqueue.append(number)
                    else:
                        minqueue.append(number)
                    
        else:
            if number == 1: # 우선순위가 높은 숫자를 삭제
                if maxqueue:
                    maxqueue.popleft()
                elif minqueue:
                    minqueue.popleft()
            else:
                if minqueue: # 우선순위가 낮은 숫자를 삭제
                    minqueue.pop()
                elif maxqueue:
                    maxqueue.pop()
                    
    if minqueue or maxqueue:
        if maxqueue:
            print(maxqueue[0], end=' ')
        else:
            print(minqueue[0], end=' ')
            
        if minqueue:
            print(minqueue[-1], end =' ')
        else:
            print(maxqueue[-1], end=' ')
    else:
        print("EMPTY")
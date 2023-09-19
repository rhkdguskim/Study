# https://www.acmicpc.net/problem/1655
# 큐를 2개로 문제를 해결한다.
# 왼쪽 오른쪽 한번씩 번갈아가면서 큐를 추가한다.
from collections import deque

leftq = deque()
rightq = deque()
initq = []
N = int(input())
counter = 0

for _ in range(N):
    number = int(input())
    counter += 1
    if counter == 1:
        leftq.append(number)
        rightq.append(number)
    elif counter == 2:
        if number > rightq[0]:
            rightq[0] = number
        else:
            rightq.pop()
            if leftq[-1] > number:
                leftq.appendleft(number)
            else:
                leftq.append(number)
    else:
        if leftq[-1] > number:
            leftq.appendleft(number)
        else:
            if rightq[0] > number:
                rightq.appendleft(number)
            else:
                rightq.append(number)
    
    print(leftq, rightq)
    
    if counter > 2:
        if counter % 2 == 0:
            while (len(leftq) != len(rightq)): # 짝수일때
                if len(leftq) > len(rightq):
                    newnum = leftq.pop()
                    if rightq[0] >= number:
                        rightq.appendleft(newnum)
                    else:
                        rightq.append(newnum)
                else:
                    newnum = rightq.popleft()
                    if leftq[-1] > newnum:
                        leftq.append(newnum)
                    else:
                        leftq.appendleft(newnum)
            
            print(min(leftq[-1], rightq[0]))
        else:
            while (abs(len(leftq) - len(rightq)) != 1): # 홀수일때
                print(leftq, rightq)
                if len(leftq) > len(rightq):
                    rightq.appendleft(leftq.pop())
                else:
                    leftq.appendleft(rightq.popleft())
                    
            if len(leftq) > len(rightq):
                print(leftq[-1])
            else:
                print(rightq[0])
    else:
        print(min(leftq+rightq))

    print(leftq, rightq)
# https://www.acmicpc.net/problem/1744
import heapq
N = int(input())

queue = []
queue2 = []
queue3 = []
for _ in range(N):
    number = int(input().rstrip())
    if number > 0:
        queue.append(number) # 양의 정수 집합
    elif number == 0:
        queue3.append(0) # 0 의 집합
    else :
        queue2.append(number) # 음의 정수 집합

queue.sort(reverse=True)
queue2.sort()
result = 0

while queue:
    number = queue.pop(0)
    if not queue or number == 1:
        result += number
    else:
        number2 = queue.pop(0)
        if number2 == 1:
            result += number + number2
        else :
            result += number * number2

if len(queue2) % 2 == 1: # 홀수이고 0이 있는 큐가 하나라도 존재하면 하나 뺀다
    number = queue2.pop()
    if not queue3:
        result += number
      
while queue2:
    number = queue2.pop(0)
    number2 = queue2.pop(0)
    
    result += number * number2
    
print(result)
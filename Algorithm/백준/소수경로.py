# https://www.acmicpc.net/problem/1963
import sys
input = sys.stdin.readline
from collections import deque

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for _ in range(int(input())):
    num1, num2 = map(int, input().split())
    visited = set([num1])
    queue = deque()
    queue.append((num1, 0))
    while queue:
        num, cost = queue.popleft()
        if num == num2:
            print(cost)
            
        for n in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            for i in range(4):
                temp = list(str(num))
                if temp[i] != str(n):
                    temp[i] = str(n)
                    new_number = int(''.join(temp))
                    if new_number >= 1000 and is_prime(new_number):
                        if not new_number in visited:
                            visited.add(new_number)
                            queue.append((new_number, cost + 1))
    
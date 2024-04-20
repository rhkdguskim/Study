# https://www.acmicpc.net/problem/10828
# 스택의 자료구조를 이해하는 문제이며, 조건에 따라서 구현만 하면 된다.
import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    temp = list(map(str, input().split()))
    if temp[0] == 'push':
        num = int(temp[1])
        stack.append(num)
    else:
        if temp[0] == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)
        elif temp[0] == 'size':
            print(len(stack))
        elif temp[0] == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        elif temp[0] == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
    
    
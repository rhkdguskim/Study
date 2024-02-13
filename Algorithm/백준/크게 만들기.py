# https://www.acmicpc.net/problem/2812
import sys
input = sys.stdin.readline

N, K  = map(int, input().split())
num = input()

stack = []
stack.append(num[0])

cnt = 0
for i in range(1, N):
    while stack and int(stack[-1]) < int(num[i]) and cnt < K:
        stack.pop()
        cnt += 1
        
    stack.append(num[i])

# 2 1
# 11 일때 예외 발생.
while cnt < K:
    cnt += 1
    stack.pop()
    
print(''.join(stack))
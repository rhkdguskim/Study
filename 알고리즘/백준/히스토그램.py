# https://www.acmicpc.net/problem/1725
import sys
input = sys.stdin.readline

N = int(input())

data = [int(input()) for _ in range(N)]

data.append(0) # 마지막 모든 데이터를 pop시키기 위해서 추가함.

stack = []
max_ans = 0

for i in range(len(data)):
    while stack and data[stack[-1]] > data[i]:
        idx = stack.pop()
        
        if not stack:
            width = i
        else:
            width = i - stack[-1] - 1
        
        max_ans = max(max_ans, width * data[idx])
        
    stack.append(i)
    
print(max_ans)
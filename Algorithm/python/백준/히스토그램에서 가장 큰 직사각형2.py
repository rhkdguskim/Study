# https://www.acmicpc.net/problem/6549
# 최소 높이와 left와 right의 크기를 알면 직사각형의 넓이를 저장 할 수 있다.

import sys
input = sys.stdin.readline

while True:
    data = list(map(int, input().split()))
    if data.pop(0) == 0:
        break
    
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
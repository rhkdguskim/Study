# https://www.acmicpc.net/problem/2493
N = int(input())
table = list(map(int, input().split()))

result = []
stack = []
stack.append([table[0], 1])
result.append(0) # 첫번째 인덱스는 레이저를 수신할 탑이 없다.
    

for i in range(1, len(table)):
    
    while stack and stack[-1][0] < table[i]:
        stack.pop()
    
    if stack:
        result.append(stack[-1][1])
    else:
        result.append(0)
        
    stack.append([table[i], i+1])

print(*result)
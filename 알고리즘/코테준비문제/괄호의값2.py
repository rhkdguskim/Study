# https://www.acmicpc.net/problem/2504
char = input()

stack = []
temp = 1
result = 0
errorFlag = False
for i in range(len(char)):
    if char[i] == '(':
        stack.append(char[i])
        temp *= 2
    elif char[i] == '[':
        stack.append(char[i])
        temp *= 3
    elif char[i] == ')':
        if not stack or stack[-1] == '[':
            errorFlag = True
            break
        
        if char[i-1] == '(':
            result += temp
        
        stack.pop()
        temp //= 2
            
    elif char[i] == ']':
        if not stack or stack[-1] == '(':
            errorFlag = True
            break
        
        if char[i-1] == '[':
            result += temp
            
        stack.pop()
        temp //= 3
        
if stack or errorFlag:
    print(0)
else:
    print(result)
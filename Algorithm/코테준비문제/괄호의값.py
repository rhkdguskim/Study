# https://www.acmicpc.net/problem/2504
char = input()

isValied = True
def dfs(arr):
    if not arr:
        return 0
        
    global isValied
    if len(arr) == 2:
        if arr[0] == '(':
            if arr[-1] == ']':
                isValied = False
                return 0
            else:
                return 2
        elif arr[0] == '[':
            if arr[-1] == ')':
                isValied = False
                return 0
            else:
                return 3
        else: # 올바르지 못한 값
            isValied = False
    
    result = 0
    startidx = 0
    for i in range(1, len(arr)):
        if arr[startidx] == "(":
            check = ')'
        else:
            check = ']'
        
        if i % 2 == 1 and check == arr[i]: # 짝수값이고 괄호가 닫혔다면
            if arr[startidx:i+1] == arr: # 곰셈 로직
                if arr[startidx] == '(':
                    result += dfs(arr[1:len(arr)-1]) * 2
                else:
                    result += dfs(arr[1:len(arr)-1]) * 3
            else:
                result += dfs(arr[startidx:i+1])
                startidx = i+1
                
    return result

answer = 0

if len(char) % 2 == 0:
    answer = dfs(char)
    
if isValied:
    print(answer)
else:
    print(0)
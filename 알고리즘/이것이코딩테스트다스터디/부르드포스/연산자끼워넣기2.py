#https://www.acmicpc.net/problem/14888
N = int(input())
numlist = list(map(int, input().split()))
oplen = list(map(int, input().split()))

sumop = list('+' for _ in range(oplen[0]))
subop = list('-' for _ in range(oplen[1]))
mulop = list('*' for _ in range(oplen[2]))
divop = list('//' for _ in range(oplen[3]))

maxvalue = int(-10e9)
minvalue = int(10e9)
def dfs(depth, result):
    global maxvalue
    global minvalue
    if len(sumop):
        sumop.pop()
        result += numlist[depth]
        dfs(depth+1, result)
        sumop.append('+')
        
    if len(subop):
        subop.pop()
        result -= numlist[depth]
        dfs(depth+1, result)
        subop.append('-')
        
    if len(mulop):
        mulop.pop()
        result *= numlist[depth]
        dfs(depth+1, result)
        mulop.append('*')
        
    if len(divop):
        divop.pop()
        result //= numlist[depth]
        dfs(depth+1, result)
        divop.append('//')
    
    if depth == N-1:
        maxvalue = max(maxvalue, result)
        minvalue = min(minvalue, result)
        return
    

dfs(1,numlist[0])

print(maxvalue)
print(minvalue)
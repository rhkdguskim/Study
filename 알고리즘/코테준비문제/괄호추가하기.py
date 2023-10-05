# https://www.acmicpc.net/problem/16637
N = int(input())
data = input()

def calculate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '*':
        return num1 * num2
    else:
        return num1 - num2

maxresult = -int(1e9)
def dfs(idx, prev):
    if idx >= N:
        global maxresult
        maxresult = max(prev, maxresult)
        return

    if idx+3 < N:
        # 바로 다음것 부터 연산한다.
        dfs(idx+4, calculate(prev, calculate(int(data[idx+1]), int(data[idx+3]), data[idx+2]), data[idx]))

    # 자기자신부터 연산한다.
    dfs(idx + 2, calculate(prev, int(data[idx + 1]), data[idx]))

if N == 1:
    print(data[0])
else:
    dfs(1, int(data[0]))
    print(maxresult)

N = int(input())
data = input()
oper = []
for i in range(len(data)):
    if not data[i].isdigit():
        oper.append((data[i], i))



maxvalue = -int(10e9)
# 3+8*7-9*2
def calculate(num1, num2, op):

    print(num1, num2, op, visited)
    if op == "*":
        return num1 * num2
    elif op == "+":
        return num1 + num2
    elif op == '-':
        return num1 - num2
def dfs(prev, visited, cursor):
    global maxvalue
    if all(visited):
        print(prev)
        maxvalue = max(maxvalue, prev)
        return

    for i in range(len(oper)):
        if not visited[i] and abs(cursor - i) == 1:
            op = oper[i][0]
            visited[i] = True
            if cursor > i:
                cur = int(data[oper[i][1]-1])
                dfs(calculate(prev, cur, op), visited, i)
            else:
                cur = int(data[oper[i][1]+1])
                dfs(calculate(prev, cur, op), visited, i)
            visited[i] = False

visited = [False] * len(oper)
for i in range(len(oper)):
    if not visited[i]:
        op = oper[i][0]
        prev = int(data[oper[i][1]-1])
        cur = int(data[oper[i][1]+1])
        visited[i] = True
        dfs(calculate(prev, cur, op), visited, i)
        visited[i] = False

print(maxvalue)
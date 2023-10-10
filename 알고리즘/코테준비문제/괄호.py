# https://www.acmicpc.net/problem/9012
T = int(input())
for _ in range(T):
    char = input()
    stack = []
    flag = True

    for i in range(len(char)):
        if char[i] == '(':
            stack.append('(')
        else:
            if stack:
                if stack[-1] == ')': # ') )' 가 연속으로 나온경우
                    flag = False
                    break

                t = stack.pop() # 짝을꺼낸다.
            else: # ')' 가 먼저 들어온경우
                flag = False
                break

    if stack: # 짝을 맞추어 다 꺼내지도 못했을 경우
        flag = False

    if flag:
        print("YES")
    else:
        print("NO")



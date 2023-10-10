# https://www.acmicpc.net/problem/14719
from pprint import pprint
H, W = map(int, input().split())
table = [[0 for _ in range(W)] for _ in range(H)]
temp = list(map(int, input().split()))

for i in range(len(temp)):
    h = temp[i]
    for j in range(h):
        table[j][i] = 1
total = 0
for i in range(H):
    stack = []
    for j in range(W):
        cur = table[i][j] # 현재
        if stack: # 스택에 값이 있는경우
            if stack[-1] == 0 and cur == 1: # 바로이전이 빗물이고, 현재 벽을 만난경우
                cnt = 0
                while stack: # 벽이 나올때까지 pop 한다
                    t = stack.pop()
                    if t == 1: # 벽이 나온경우 종료하고 cnt를 반영한다.
                        total += cnt
                        stack = [] # 스텍을 초기화
                    if t == 0: # 빗물인경우 빗물의 개수를샌다
                        cnt += 1

        stack.append(cur)

print(total)



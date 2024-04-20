# https://www.acmicpc.net/problem/1022
# 그래프를 (0, 0)으로 시작해서 (N, N)으로 끝나는 그래프로 바꿔서 생각한다.

import sys

input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().split())
R = r2 - r1 + 1
C = c2 - c1 + 1

fill_cnt = R*C

table = [[0 for _ in range(C)] for _ in range(R)]

moves = [(0, 1), (-1, 0), (0, -1), (1, 0)] # right, up, left, down

def chage_dir(dir):
    if dir == 3:
        return 0
    else:
        return dir + 1
    
y = - r1
x = - c1
i = 1
cnt = 1
dir = 0
max_length = 0
while fill_cnt > 0:
    for _ in range(2):
        for _ in range(i):
            if R > y >=0 and C > x >=0:
                max_length = len(str(cnt))
                table[y][x] = str(cnt)
                fill_cnt -= 1
            
            y += moves[dir][0]
            x += moves[dir][1]
            cnt += 1
        
        dir = chage_dir(dir)
    
    i += 1
    
for i in range(R):
    for j in range(C):
        length = len(table[i][j])
        if max_length > length:
            table[i][j] = ' '*(max_length-length) + table[i][j]

for t in table:
    print(*t)
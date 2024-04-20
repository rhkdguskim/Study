# https://www.acmicpc.net/problem/20056
# 각자의 위치에서 대기한다.
import sys
from collections import defaultdict
input = sys.stdin.readline

N, M, K = map(int, input().split())
moves = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
direction = [(0, 2, 4, 6), (1, 3, 5, 7)]

def chage_dir(y, x):
    y = (y + N) % N
    x = (x + N) % N
    return y, x
        
fire_ball = []
for _ in range(M):
    # 위치, 질량, 속도, 방향
    r, c, m, s, d = map(int, input().split())
    fire_ball.append([r-1, c-1, m, s, d])

def move_fire_ball(fire_ball):
    new_fire_ball = []
    table = defaultdict(list)
    
    for y, x, m, s, d in fire_ball:
        y, x = chage_dir(y + moves[d][0]*s, x + moves[d][1]*s)
        table[(y, x)].append((m, s, d))
        
    for key in table.keys():
        y, x = key
        if len(table[key]) >= 2:
            sum_m = 0
            sum_s = 0
            odd = 0
            even = 0
            for nm, ns, nd in table[key]:
                sum_m += nm
                sum_s += ns
                if nd % 2 == 0:
                    even += 1
                else:
                    odd += 1
                    
            new_m = sum_m // 5
            new_s = sum_s // len(table[key])
            if new_m > 0:
                if even == 0 or odd == 0:
                    new_d = 0
                else:
                    new_d = 1
                for i in range(4):
                    new_fire_ball.append([y, x, new_m, new_s, direction[new_d][i]])

        else:
            m, s, d = table[key][0]
            new_fire_ball.append([y, x, m, s, d])
    
    return new_fire_ball
            
for _ in range(K):
    fire_ball = move_fire_ball(fire_ball)
    
print(sum(m[2] for m in fire_ball))
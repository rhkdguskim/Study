# https://www.acmicpc.net/problem/15997
# KOREA CCC BBB AAA
# KOREA CCC 1.0 0.0 0.0
# AAA BBB 0.428 0.144 0.428
# AAA KOREA 0.0 0.0 1.0
# CCC BBB 0.0 0.0 1.0
# KOREA BBB 1.0 0.0 0.0
# CCC AAA 0.0 0.0 1.0

countrys = list(map(str, input().split()))
score = dict()
statuses = ['win','lose', 'draw']
for country in countrys:
    score[country] = float(0)

for _ in range(6):
    A, B, W, D, L = map(str, input().split())
    # 이겻을때 비겼을때 졌을때 3가지를 모두 고려해야한다.
    
    for status in statuses:
        if status == 'win': # A가 B를 이겼을경우
            score[A] += 3*float(W) # A만 승점 3점
            pass
        elif status == 'lose': # A가 B에게 졌을경우
            score[B] += 3*float(L)
        else: # A와 B가 비겼을경우
            score[A] += 3*float(D)
            score[B] += 3*float(D)
            

print(score)
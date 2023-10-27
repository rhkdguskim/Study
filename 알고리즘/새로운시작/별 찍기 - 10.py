# https://www.acmicpc.net/problem/2447
from copy import deepcopy
k = int(input())

n = 1
star = ['' for _ in range(3)]
while n > k:
    newstar = ['' for _ in range(3)]
    if n == 1: # 초기
        newstar[0] = '*'*3
        newstar[1] = '*' + ' ' + '*'
        newstar[2] = '*'*3
    else: # 이전에 있던 star 값을 사용
        for n in range(3):
            for s in star[n]:
                if n == 1:
                    pass
                else:
                    newstar[n] += s
                    newstar[n] += '\n'
        
    star = deepcopy(newstar)
    n *= 3
# https://www.acmicpc.net/problem/17825
from copy import deepcopy
dice = list(map(int, input().split()))
table = [False for _ in range(50)]

ans = 0
def dfs(order, horse):
    global ans
    if len(order) == 10: # 최종 스코어
        total = 0
        for i in range(1,5):
            total += horse[i][2]

        ans = max(total, ans)
        return

    result = 0
    for i in range(1, 5): # 순서 경우의 수
        temp = []
        for j in range(1,5):
            if horse[j][0]:
                temp.append(horse[j][0])

        if 40 >= horse[i][0]: # 도착하지 않은 말인경우
            cost = dice[len(order)]
            prevpos = horse[i][0]
            prevtype = horse[i][1]

            pos = horse[i][0]
            type = horse[i][1]

            for _ in range(cost): # 주사위 횟수만큼 반복문 이행
                if pos >= 40: # 40의 위치에 있다면 주사위와 상관없음
                    pos += 1
                    break

                if type == 0:
                    pos += 2 # 일반 움직임
                elif type == 1: # 10에서 시작할경우
                    if 16 >= pos >= 10:
                        pos += 3
                    elif pos == 19:
                        pos += 6
                    else:
                        pos += 5
                elif horse[i][1] == 2: # 20에서 시작할경우
                    if 22 >= pos >=20:
                        pos += 2
                    elif pos == 24:
                        pos += 1
                    else:
                        pos += 5
                elif horse[i][1] == 3: # 30에서 시작할경우
                    if 30 >= pos >=26:
                        pos -= 1
                    else:
                        pos += 5

            if pos == 10: # 10의 위치에 도달하면
                type = 1
            elif pos == 20 : # 20의 위치에 도달하면
                type = 2
            elif pos == 30: # 30의 위치에 도달하면
                type = 3

            if pos in temp:  # 해당위치에 말이 있는경우
                return

            horse[i][0] = pos
            horse[i][1] = type
            horse[i][2] += pos # 자기 위치의 점수를 반영한다.
            order.append(i)
            dfs(order, horse)
            horse[i][0] = prevpos
            horse[i][1] = prevtype
            horse[i][2] -= pos
            order.pop()


horse = [[0, 0, 0] for _ in range(5)] # 자기 위치, type, 최종스코어
dfs([], horse)
print(ans)
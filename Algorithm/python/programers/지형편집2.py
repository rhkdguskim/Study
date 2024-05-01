# https://school.programmers.co.kr/learn/courses/30/lessons/12984
from itertools import chain

def solution(land, P, Q):
    land = list(chain.from_iterable(land))
    land.sort()
    n = len(land)

    # Q의 맥스값부터 시작해서 높이가 달라질때마다 값을 갱신한다.
    cost = sum([land[i] - land[0] for i in range(1, n)]) * Q
    answer = cost

    for i in range(1, n):
        # 높이가 달라진다면 이제 P가중치를 증가, Q가중치를 감소시킨다.
        if land[i] != land[i-1]:
            h = land[i] - land[i-1]
            cost += h*(i*P) - h*(n-i)*Q
            answer = min(cost, answer)

    return answer
import math

def solution(n, stations, w):
    answer, start = 0, 1
    # 전파가 안되는 마을의 구간을 구한다.
    for cur in stations:
        length = cur - w - start
        answer += math.ceil(length / (w*2 + 1))
        start = cur + w + 1

    if n >= start:
        length = n + 1 - start
        answer += math.ceil(length / (w * 2 + 1))

    return answer
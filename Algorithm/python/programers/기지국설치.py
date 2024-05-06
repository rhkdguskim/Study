# https://school.programmers.co.kr/learn/courses/30/lessons/12979
# 1. 구간을 나눈다.
# 2. 전파값이 i이면 1+ i*2 만큼 전파가 됨
# 3. 마을의 길이(N) // 전파값(1+ i*2) = 기지국 수

from math import ceil

def solution(n, stations, w):
    def make(city):
        return [max(0, city - w), min(city + w, n)]

    # 해당위치를 기준으로 기지국의 범위를 지정한다.
    temp = [[0, 0]] + list(map(make, stations)) + [[n+1, n+1]]
    n = len(temp)

    # 도시의 구간을 나눈다.
    city_range = set()

    # 겹치는 부분을 제거 해가면서 도시의 구간을 나누어본다.
    for i in range(1, n-1):
        if temp[i-1][1] < temp[i][0]:
            city_range.add((temp[i-1][1] + 1, temp[i][0] - 1))

        if temp[i+1][0] > temp[i][1]:
            city_range.add((temp[i][1] + 1, temp[i+1][0] - 1))

    answer = 0

    # 도시의 구간을 길이를 구하여 기지국을 설치할 최소 수를카운팅 한다.
    for r in city_range:
        length = r[1] - r[0] + 1
        answer += ceil(length / (1 + w*2))

    return answer
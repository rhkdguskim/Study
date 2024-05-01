# https://school.programmers.co.kr/learn/courses/30/lessons/12984

# 지형이 주어지면 가장 낮은 층부터 가장 높은층까지 모두 만들어보면서 가중치의 값이 가장 작은값을 갱신한다.
# 블록의 높이가 10억임으로 1 부터 최대 10억까지 탐색을 해봐야 함으로 log N의 알고리즘을 찾아야한다. ( 이분탐색, 우선순위 큐 )
# 높이를 높히면 P의 값이 늘어나고, 높이를 낮추면 Q의 값이 늘어난다.
# 높이를 조절해가면서 P의 합과 Q의 합을 비교해서 P의 합이 더 높다면 높이를 낮추고, Q의 합이 더 높다면 높힌다.
# 만약 P의 합과 Q의 합이 같다면?
# P와 Q의 합이 가중치 값이다.

# 추가는 P, 삭제는 Q
# P는 높이를 낮추면 값이 변하지 않는다.
# Q는 높이를 높이면 값이 변하지 않는다.

# P의 합이 더 크다면, 높이를 높여본다.
# Q의 합이 더 크다면, 높이를 낮추어본다.

import sys


def solution(land, P, Q):
    min_h = sys.maxsize
    max_h = 0

    for row in land:
        min_h = min(min_h, min(row))
        max_h = max(max_h, max(row))

    answer = sys.maxsize

    while min_h <= max_h:
        mid = (min_h + max_h) // 2
        add_cost = 0
        remove_cost = 0

        for row in land:
            for height in row:
                if height < mid:
                    add_cost += (mid - height) * P
                elif height > mid:
                    remove_cost += (height - mid) * Q

        current_cost = add_cost + remove_cost
        answer = min(answer, current_cost)

        if add_cost < remove_cost:
            min_h = mid + 1
        else:
            max_h = mid - 1

    return answer

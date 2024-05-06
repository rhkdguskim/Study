# https://school.programmers.co.kr/learn/courses/30/lessons/68646
# 임의의 풍선 2개를 골라서 한개의 풍선을 터트림 ( 두 풍선을 골라서 번호가 더 작은 풍선은 최대 1번만 가능 )
# 터트린뒤, 남은 풍선들 중앙으로 밀집시킴

# 자기자신을 기준으로 왼쪽 풍선들 오른쪽 풍선들을 생각해본다.
# 1. 왼 : 큼, 우 : 큼 -> 살아남음
# 2. 왼 : 작, 우 : 큼 -> 살아남음
# 3. 왼 : 큼, 우 : 작 -> 살아남음
# 4. 왼: 작, 우 : 작 -> 살아남지 못함.

# [-16,27,65,-2,58,-92,-71,-68,-61,-33]
# [9,-1,-5]
import sys

def solution(a):
    min_value = sys.maxsize
    answer = []

    for n in a:
        while len(answer) > 1 and answer[-1] > min_value and answer[-1] > n:
            answer.pop()

        min_value = min(n, min_value)
        answer.append(n)


    return len(answer)
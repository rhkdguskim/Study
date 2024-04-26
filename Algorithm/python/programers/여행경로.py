# https://school.programmers.co.kr/learn/courses/30/lessons/43164
from collections import defaultdict
import heapq

# 1개 일경우 큐에 넣는다.
# 다음에 방문할 수 있는 알파벳중에서 알파벳순서가 가장 가까운 알파벳을 꺼낸다.
def solution(tickets):
    routes = defaultdict(list)
    # 딕셔너리에 입력을받는다.
    for s, t in tickets:
        heapq.heappush(routes[s], t)

    answer = ['ICN']

    while routes[answer[-1]]:
        dest = heapq.heappop(routes[answer[-1]])
        answer.append(dest)

    return answer
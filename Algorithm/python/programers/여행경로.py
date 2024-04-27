# https://school.programmers.co.kr/learn/courses/30/lessons/43164
from collections import defaultdict

# 1개 일경우 큐에 넣는다.
# 다음에 방문할 수 있는 알파벳중에서 알파벳순서가 가장 가까운 알파벳을 꺼낸다.
def solution(tickets):
    routes = defaultdict(list)
    # 딕셔너리에 입력을받는다.
    for s, t in tickets:
        routes[s].append(t)

    # 알파벳이 가장 빠른순으로 pop 해야하기때문.
    for key in routes.keys():
        routes[key].sort(reverse=True)

    answer = []
    path = ['ICN']
    while path:
        now = path[-1]
        # 더이상 갈 수 없는 위치라면 마지막 경로이다.
        if not routes[now]:
            answer.append(path.pop())
        else:
            path.append(routes[now].pop())

    return answer[::-1]
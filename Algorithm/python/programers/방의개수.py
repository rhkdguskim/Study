# https://school.programmers.co.kr/learn/courses/30/lessons/49190

# 새로운 간선이 추가되고 기존에 방문했던 노드를 재차 방문할경우 ( 단, 간선의 수가 3이상이어야함.  양방향을 체크 함으로 4이상을 체크해야함 )
def solution(arrows):
    moves = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    nodes = set()
    edges = set()

    start_y = 0
    start_x = 0

    nodes.add((start_y, start_x))
    answer = 0

    # 한번 지나왔던 점으로 다시 연결될때 방이 하나 만들어집니다.
    # 대각선으로 크로스 연결될때 방이 2개가 추가됩니다.

    for i in arrows:
        new_y = moves[i][0] + start_y
        new_x = moves[i][1] + start_x

        if (new_y, new_x) in nodes:
            if (start_y, start_x, new_y, new_x) not in edges and 4 <= len(edges):
                answer += 1

        # 양방향을 체크해준다.
        edges.add((start_y, start_x, new_y, new_x))
        edges.add((new_y, new_x, start_y, start_x))

        nodes.add((new_y, new_x))

        start_y = new_y
        start_x = new_x

    return answer
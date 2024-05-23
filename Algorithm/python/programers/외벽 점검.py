# https://school.programmers.co.kr/learn/courses/30/lessons/60062
# 가장 많이 걸어갈 수 있는친구부터 간다.
# 거리가 가장 멀리 떨어진 외벽순으로 방문하여 없앤다.
# 1. 가장 많이 갈 수 있는 친구부터 순회한다.
# 2. 각 취약 지점의 양 옆으로 거리 차이를 구한다.
# 3. 취약 지점이 가장 큰 노드를 찾는다.
# 4. 다음 취약지점을 구한다.
#    만약 이동 할 수 없다면 종료
#    다 이동했다면 1번으로 간다.
#    더 이동 할 수 있다면 2번으로 간다.

def solution(n, weak, dist : list):
    def get_distance_with_max(weak):
        s = len(weak)
        d = [[0, 0] for _ in range(s)]
        for i in range(s):
            if i == 0:
                cost = weak[i] + n - weak[-1]
                dist[-1][0] = cost
            else:
                cost = weak[i] - weak[i-1]
                dist[i-1][0] = cost
                
            d[i][1] = cost
        return d
    
    distance = get_distance_with_max(weak)
    length = len(distance)
    for i in range(length):
        
        
    return cnt
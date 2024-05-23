# https://school.programmers.co.kr/learn/courses/30/lessons/72413

# 플로이드 워셜로 각 모든 구간의 최단거리를 구한다.
# 그런다음 s -> i(특정노드) 에서 각각 a, b 로 모든 경우의 수중에서 최소값을 고르면 끝
import sys

def solution(n, s, a, b, fares):
    distance = [[sys.maxsize] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        distance[i][i] = 0
        
    for c, d, f in fares:
        distance[c][d] = f
        distance[d][c] = f
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                distance[i][j] = min(distance[i][k]+distance[k][j], distance[i][j])
    
    answer = distance[s][a] + distance[s][b]
    for i in range(1, n+1):
        answer = min(answer, distance[s][i] + distance[i][a] + distance[i][b])
        
    return answer
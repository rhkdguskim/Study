# https://school.programmers.co.kr/learn/courses/30/lessons/87391
# 다이나믹 프로그래밍 문제.
# 해당 위치에서 같은 경로탐색이 이미 방문되어있다면 방문할 필요가 없다.


# 거꾸로 탐색해본다.
# x,y 위치에서 다른위치로 갈 수 있는 경우의 수

# (0, 0)
# ㅗ -> <- -> <- ㅗ
def solution(n, m, x, y, queries):
    
    answer = -1
    return answer
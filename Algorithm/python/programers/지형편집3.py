import sys
from collections import defaultdict

def solution(land, P, Q):
    n = len(land)
    height = defaultdict(int)
    for i in range(n):
        for j in range(n):
            height[land[i][j]] += 1

    def cal(h):
        p_cnt = 0
        q_cnt = 0

        for key in height.keys():
            if h > key:
                p_cnt += (h - key) * height[key]
            elif h < key:
                q_cnt += (key - h) * height[key]

        return p_cnt * P + q_cnt * Q

    start = 0
    end = max(height)
    answer = sys.maxsize
    while True:
        mid = (start + end) // 2

        d_value = cal(mid-1)
        m_value = cal(mid)
        u_value = cal(mid+1)

        if m_value <= d_value and m_value <= u_value:
            answer = min(answer, m_value)
            break
        elif d_value < m_value:
            end = mid - 1
        elif u_value < m_value:
            start = mid + 1

    return answer

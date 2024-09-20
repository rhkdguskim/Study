import heapq
from itertools import combinations_with_replacement

# 명수마다 배정하는 결과는 항상 동일하다.

def solution(k, n, reqs):
    # 각 멘토 유형에 최소 1명씩 배정
    mentors = [1 for _ in range(k)]
    dp = [[-1 for _ in range(len(reqs) + 1)] for _ in range(k)]
    q = [list(filter(lambda x: x[2] == m+1, reqs)) for m in range(k)]
    n -= k  # 각 유형에 1명씩 배정했으므로 남은 인원 n에서 k를 뺀다.

    def calculate(mentors):
        total = 0
        for m in range(k):
            mentors_cnt = mentors[m]
            if dp[m][mentors_cnt] == -1:
                total_delayed = 0
                schdule = [0 for _ in range(mentors_cnt)]
                # 요청시간, 상담시간
                for a, b, _ in q[m]:
                    time = heapq.heappop(schdule)
                    delayed_time = max(0, time - a)
                    # 기다림 없이 바로 업데이트
                    if delayed_time == 0:
                        heapq.heappush(schdule, a + b)
                    # 기다린시간 + 요청시간
                    else:
                        total_delayed += delayed_time
                        heapq.heappush(schdule, time + b)

                dp[m][mentors_cnt] = total_delayed
                
            total += dp[m][mentors_cnt]
        
        return total

    # 가능한 총합이 n인 배정 조합을 생성
    combinations = combinations_with_replacement(range(k), n)

    min_v = float('inf')
    
    # 가능한 모든 멘토 배정에 대해 최소 지연 시간을 계산
    for comb in combinations:
        print(comb)
        # 각 유형에 할당된 추가 멘토 수를 반영
        mentors_comb = mentors[:]
        for i in comb:
            mentors_comb[i] += 1  # 각 유형에 멘토를 할당
        
        min_v = min(min_v, calculate(mentors_comb))

    return min_v

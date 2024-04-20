# https://school.programmers.co.kr/learn/courses/30/lessons/118668
import heapq

# 알고리즘공부, 코딩공부, (문제풀기) 세개의 분기사항으로 시간을 추가하며 우선순위큐 탐색한다. ( 최대 힙큐 )
def solution(alp, cop, problems):
    answer = 0
    queue = []
    heapq.heappush(queue, (0, alp, cop))
    
    max_alp = 0
    max_cop = 0
    
    for alp_req, cop_req, _, _, _ in problems:
        max_alp = max(alp_req, max_alp)
        max_cop = max(max_cop, cop_req)
    print(max_alp, max_cop)
    
    answer = 201
    while queue:
        time, q_alp, q_cop = heapq.heappop(queue)
        
        if q_alp >= max_alp and q_cop >= max_cop:
            answer = min(-time, answer)
        
        if -time > answer:
            continue
        
        
        heapq.heappush(queue, (time -1, q_alp+1, q_cop))
        heapq.heappush(queue, (time -1, q_alp, q_cop + 1))
        
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if q_alp >= alp_req and q_cop >= cop_req:
                heapq.heappush(queue, (time-cost, alp_rwd + q_alp, cop_rwd + q_cop))
        
        
    return answer

MAX_ALP = 150
MAX_COP = 150
MAX_PROBLEM = 100
MAX_COST = 100
MAX_TIME = MAX_COST * MAX_PROBLEM
INF = int(10e9)
# 다이나믹 프로그래밍 문제해결
def solution(alp, cop, problems):
    dp = [[float('inf') for _ in range(MAX_ALP + 1)] for _ in range(MAX_COP+1)]
    max_alp = 0
    max_cop = 0
    
    for alp_req, cop_req, _, _, _ in problems:
        max_alp = max(alp_req, max_alp)
        max_cop = max(max_cop, cop_req)
        
        
    dp[alp][cop] = 0
    
    for i in range(alp, MAX_ALP+1):
        for j in range(cop, MAX_COP+1):
            if i + 1 <= MAX_ALP:
                dp[i+1][j] = min (dp[i+1][j],dp[i][j] + 1)
            if j + 1 <= MAX_COP:
                dp[i][j+1] = min (dp[i][j+1], dp[i][j] + 1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    temp_i = min(MAX_ALP, i + alp_rwd)
                    temp_j = min(MAX_COP, j + cop_rwd)
                    dp[temp_i][temp_j] = min(dp[temp_i][temp_j], dp[i][j] + cost)
    
    return dp[max_alp][max_cop]

    
def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    for a,b,c,d,e in problems:
        max_alp = max(max_alp,a)
        max_cop = max(max_cop,b)
    # max_alp,max_cop 가  초기값보다 낮을수도있으므로 세팅
    alp = min(alp,max_alp)
    cop = min(cop,max_cop)
    INF = float('inf')
    dp = [[INF]*(max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            # 배열 범위벗어나지않게 
            if i + 1 <= max_alp:
                dp[i + 1][j    ] = min (dp[i + 1][j    ],dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i    ][j + 1] = min (dp[i    ][j + 1],dp[i][j] + 1)

            # 모든문제 순회 하면서 
            for alp_req,cop_req,alp_rwd,cop_rwd,cost in problems:
                # 현재 i,j 로 풀수있다면
                if i >= alp_req and j >= cop_req:
                    # 풀어서 얻은 내 최종 알고,코딩력이 max_alp,max_cop 보다크면 그대로 max_alp,max_cop 에 저장 
                    next_alp,next_cop = min(max_alp,i + alp_rwd), min(max_cop,j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop],dp[i][j] + cost)
    return dp[-1][-1]

alp = 10
cop = 10
problems = [[10,15,2,1,2],[20,20,3,3,4]]
print(solution(alp, cop, problems))
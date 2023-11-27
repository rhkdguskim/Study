# https://school.programmers.co.kr/learn/courses/30/lessons/42889
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]


def solution(N, stages):
    stages.sort()
    games = [0 for _ in range(N+2)]
    for stage in stages:
        games[stage] += 1
    
    answer = [(games[i]/sum(games[i:]), i) if not sum(games[i:]) == 0 else (0, i) for i in range(1, N+1)]
    answer.sort(reverse=True, key=lambda x: (x[0], -x[1]))
    ans = [answer[i][1] for i in range(len(answer))]
    return ans

print(solution(N, stages))
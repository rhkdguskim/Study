# https://www.acmicpc.net/problem/14889
# 조합을 이용한 풀이

import itertools

N = int(input())

playerscore = []
for _ in range(N):
    playerscore.append(list(map(int, input().split())))

minvalue = int(10e9)

def calculate_score(team):
    score = 0
    team_combinations = list(itertools.combinations(team, 2))
    for a, b in team_combinations:
        score += playerscore[a][b] + playerscore[b][a]
    return score

def minimize_score_difference():
    global minvalue
    half_N = N // 2
    players = set(range(N))
    
    for team1 in itertools.combinations(players, half_N):
        team1 = set(team1)
        team2 = players - team1
        score1 = calculate_score(team1)
        score2 = calculate_score(team2)
        minvalue = min(minvalue, abs(score1 - score2))
    
    return minvalue

result = minimize_score_difference()
print(result)
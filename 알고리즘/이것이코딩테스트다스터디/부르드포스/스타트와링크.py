# https://www.acmicpc.net/problem/14889
# 1. 선수들의 조합을 만든다.
# 2. 팀의 능력치를 계산하고, 차이점을 계산하여 최소값에 업데이트한다.
# 3. 다음 팀의 조합을 계산한다. 계산할때 최소값보다 커진다면 백트래킹 한다.
from itertools import combinations
N = int(input())

playerscore = []
for _ in range(N):
    playerscore.append(map(int, input().split()))

team = [i for i in range(N)]
teams = list(combinations(team, len(team)//2))

print(teams)
team1 = []
team2 = []
for player1 in teams:
    team1.append(player1)
    team2.append(tuple(player2 for player2 in team if player2 not in player1))
    
mindata = int(10e9)

print(team1)
print(team2)
# def dfs(team1, team2):
    
#     score1 = list(combinations(team1, 2))
#     score2 = list(combinations(team1, 2))
    
#     sum = 0
#     for i in range(len(score1)):
#         score1[i][0]score1[i][1]
        
# https://www.acmicpc.net/problem/14889
# 1. 선수들의 조합을 만든다. ( 재귀로 만든다. )
# 2. 팀의 능력치를 계산하고, 차이점을 계산하여 최소값에 업데이트한다.
import itertools
N = int(input())

playerscore = []
for _ in range(N):
    playerscore.append(list(map(int, input().split())))

players = [i for i in range(N)]

team1 = []
minvalue = int(10e9)
def dfs(playerscore):
    global minvalue
    if len(team1) == N // 2: # 종료조건
        score1 = 0
        score2 = 0
        team2 = []
        for player2 in players: # team2의 플레이어를 구한다
            if player2 not in team1:
                team2.append(player2)
        newteam1 = list(itertools.combinations(team1, 2))
        newteam2 = list(itertools.combinations(team2, 2))
        
        for a,b in newteam1:
            score1 += playerscore[a][b]
            score1 += playerscore[b][a]
        
        for a,b in newteam2:
            score2 += playerscore[a][b]
            score2 += playerscore[b][a]
            
        minvalue = min(minvalue, abs(score1 - score2))
        print(minvalue, newteam1, newteam2)
        return minvalue


    for i in range(N):
        if i not in team1: # 팀에 자기자신을 넣지 않는다.
            team1.append(i)
            dfs(playerscore)
            team1.pop()
            

team1.append(0)
dfs(playerscore)
team1.pop()

print(minvalue)
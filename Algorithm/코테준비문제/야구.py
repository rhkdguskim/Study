# https://www.acmicpc.net/problem/17281
N = int(input())

table = [[0 for _ in range(10)] for _ in range(N+1)]
for i in range(1, N+1):
    temp = list(map(int, input().split()))

    for j in range(1, 10):
        table[i][j] = temp[j-1]
def dfs(player):
    if len(player) == 4:
        if player[3] != 1: # 4번 타자가 1번이 아닌경우
            return 0

    if len(player) == 9: # 플레이어 9명을 다 뽑은경우
        start = 0
        ining = 1
        score = 0
        while N+1 > ining:
            out, b1, b2, b3 = 0, 0, 0, 0
            while 3 > out:
                p = player[start]
                if table[ining][p] == 0: # 아웃인경우
                    out += 1
                elif table[ining][p] == 1: # 안타인경우
                    score += b3
                    b3 = b2
                    b2 = b1
                    b1 = 1
                elif table[ining][p] == 2: # 2루타인경우
                    score += b2
                    score += b3
                    b3 = b1
                    b2 = 1
                    b1 = 0
                elif table[ining][p] == 3: # 3루타인경우
                    score += b1
                    score += b2
                    score += b3
                    b1 = 0
                    b2 = 0
                    b3 = 1
                elif table[ining][p] == 4: # 홈런인경우
                    score += b1
                    score += b2
                    score += b3
                    score += 1
                    b1 = 0
                    b2 = 0
                    b3 = 0

                start += 1
                start %= 9

            ining += 1

        return score

    maxscore = 0
    for i in range(1, 10): # 순열임으로 1, 10 까지 모두 탐색한다.
        if i not in player:
            player.append(i)
            maxscore = max(maxscore, dfs(player))
            player.pop()

    return maxscore

print(dfs([]))
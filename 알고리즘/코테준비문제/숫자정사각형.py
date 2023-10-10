# https://www.acmicpc.net/problem/1051
N, M = map(int, input().split())
table = [[0 for _ in range(M)] for _ in range(N)]
move = ((0,1), (1,0), (1,1))
for i in range(N):
    temp = list(input())
    for j in range(len(temp)):
        table[i][j] = int(temp[j])

cnt = 0
for i in range(N):
    for j in range(M):
        # 정사각형임으로 더 작은 크기까지만 계산해본다.
        if M > N:
            MAXSIZE = M
        else:
            MAXSIZE = N

        for s in range(MAXSIZE-1, -1, -1):
            temp = [False for _ in range(3)]
            for k in range(len(move)):
                ny = i + move[k][0] * s
                nx = j + move[k][1] * s

                if N > ny >= 0 and M > nx >= 0: # 정사각형 범위라면
                    if table[i][j] == table[ny][nx]: # 꼭지점이 같다면
                        temp[k] = True
            if all(temp): # 모든 꼭지점이 같다면
                cnt = max(cnt, (s+1)*(s+1))

print(cnt)
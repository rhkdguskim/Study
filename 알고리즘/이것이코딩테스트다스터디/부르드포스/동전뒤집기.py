#https://www.acmicpc.net/problem/1285
# 앞면 H 뒷면은 T
# 열과 행을 둘중하나 잡아서 뒤집을지 안뒤집을지 경우의 수를 모두 구한뒤에 열을 뒤집어가면서 최적의 해를 구한다.

N = int(input())
board = []
for _ in range(N):
    board.append(list(str(input())))

reverseboard = board[:] # 복사한다.
for i in range(N):
    for j in range(N):
        if reverseboard[i][j] == 'T':
            reverseboard[i][j] = 'H'
        else:
            reverseboard[i][j] = 'T'       

        
print(reverseboard)
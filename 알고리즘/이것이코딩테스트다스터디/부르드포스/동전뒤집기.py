#https://www.acmicpc.net/problem/1285
# 앞면 H 뒷면은 T
# 열과 행을 둘중하나 잡아서 뒤집을지 안뒤집을지 경우의 수를 모두 구한뒤에 열을 뒤집어가면서 최적의 해를 구한다.
import copy

N = int(input())
board = [] # 입력보드
for _ in range(N):
    board.append(list(str(input())))

reverseboard = copy.deepcopy(board) # 깊은 복사한다.
for i in range(N):
    for j in range(N):
        if reverseboard[i][j] == 'T': # Tail의 개수가 최적화 되어야 함으로 Tail일 경우 Head로 바꿔준다.
            reverseboard[i][j] = 'H'
        else:
            reverseboard[i][j] = 'T'       

ans = N**2
for k in range((1 << N)): # 경우의 수는 각 행이 뒤집은경우 뒤집지 않은경우 N^2 개이다. 비트마스킹으로 처리
    tempboard = []
    for i in range(N):
        if 1<<i & k :
            tempboard.append(reverseboard[i]) # 해당 행을 뒤집은 경우
        else:
            tempboard.append(board[i]) # 해당 행을 뒤집지 않은경우
            
    newans = 0
    for i in range(N):
        temp = 0
        for j in range(N):
            if tempboard[j][i] == 'T':
                temp += 1

        newans += min(temp, N- temp) # 뒤집지 않은경우, 뒤집은경우
        
    ans = min(ans, newans)
    
print(ans)
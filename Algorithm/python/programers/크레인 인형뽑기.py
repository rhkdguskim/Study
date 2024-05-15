# https://school.programmers.co.kr/learn/courses/30/lessons/64061

# 보드, 바구니 스택을 이용하여 푼다.

def solution(board, moves):
    bag = []
    
    n = len(board)
    new_board = [[] for _ in range(n)]
    
    for j in range(n):
        for i in range(n-1, -1, -1):
            if board[i][j]:
                new_board[j].append(board[i][j])
    
    answer = 0
    
    for d in moves:
        d -= 1
        if new_board[d]:
            doll = new_board[d].pop()
            
            if bag and bag[-1] == doll:
                bag.pop()
                answer += 2
            else:
                bag.append(doll)
    
    return answer
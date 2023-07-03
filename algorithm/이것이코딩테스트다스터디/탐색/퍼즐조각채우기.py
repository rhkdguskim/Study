
game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]

M = len(game_board)

empty = []
puzzle = []

move = ["up","right","down","left"]

def getMovetype(cur, next):
    i,j = cur
    n,m = next
    if n == i: 
        if m > j: 
            return move[1] # 현재 x좌표가 다음의 x좌표보다 작다면 오른쪽으로 이동한다.
        else:
            return move[3] # 현재 x좌표가 다음의 x좌표보다 크다면 오른쪽으로 이동한다.
    elif n > i :
        return move[0] # 현재 y좌표가 다음의 y좌표보다 작다면 올라간다.
    else:
        return move[2] # 현재 y좌표가 다음의 y좌표보다 크다면 내려간다.
    

def dfs(i,j, puzzle, board, visited, bpuzzle):
    if M > i >=0 and M > j >= 0 and not visited[i][j] and board[i][j] == bpuzzle:
        visited[i][j] = True
        puzzle.append([i,j])
        dfs(i+1, j, puzzle, board, visited, bpuzzle)
        dfs(i-1, j, puzzle, board, visited, bpuzzle)
        dfs(i, j+1, puzzle, board, visited, bpuzzle)
        dfs(i, j-1, puzzle, board, visited, bpuzzle)
    
    return puzzle

def getPuzzle(board, puzzles, visited, bpuzzle):
    for i in range(M):        
        for j in range(M):
            new = []
            if board[i][j] == bpuzzle:
                dfs(i,j, new, board, visited, bpuzzle)
                if len(new):
                    puzzles.append(new)
                    
                    
                    
    
def solution(game_board, table):
    visited = [[False for _ in range(M)] for i in range(M)]
    getPuzzle(game_board, empty, visited, 0) # game_board 의 퍼즐을넣을 리스트를 갱신한다.
    visited2 = [[False for _ in range(M)] for i in range(M)]
    getPuzzle(table, puzzle, visited2, 1) # table에 퍼즐리스트를 갱신한다.


solution(game_board, table)
print(puzzle)
print(empty)
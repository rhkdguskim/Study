# https://school.programmers.co.kr/learn/courses/30/lessons/92345


game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]

M = len(game_board)

empty = []
puzzle = []

move = ["up","down","right","left"]

def getMovetype(cur, next):
    i,j = cur
    n,m = next
    if n == i: 
        if m > j: 
            return move[2] # 현재 x좌표가 다음의 x좌표보다 작다면 오른쪽으로 이동한다.
        else:
            return move[3] # 현재 x좌표가 다음의 x좌표보다 크다면 오른쪽으로 이동한다.
    elif n > i :
        return move[0] # 현재 y좌표가 다음의 y좌표보다 작다면 올라간다.
    else:
        return move[1] # 현재 y좌표가 다음의 y좌표보다 크다면 내려간다.
    

def dfs(i,j, puzzle, board, visited):
    if M > i >=0 and M > j >= 0 and not visited[i][j] and board[i][j] == 1:
        visited[i][j] = True
        puzzle.append([i,j])
        dfs(i+1, j, puzzle, board, visited)
        dfs(i-1, j, puzzle, board, visited)
        dfs(i, j+1, puzzle, board, visited)
        dfs(i, j-1, puzzle, board, visited)
    
    return puzzle

def getPuzzle(board, puzzles, visited):
    for i in range(M):        
        for j in range(M):
            new = []
            if board[i][j] == 1:
                dfs(i,j, new, board, visited)
                if len(new):
                    puzzles.append(new)
                    
def moveList(puzzles):
    movelist = [[] for _ in range(len(puzzles))]
    for i in len(puzzles):
        for j in range(len(puzzles) -1):
            movelist[i].append(getMovetype(puzzles[i][j], puzzles[i][j+1]))
            
    return movelist
    
def solution(game_board, table):
    visited = [[False for _ in range(M)] for i in range(M)]
    getPuzzle(game_board, empty, visited) # game_board 의 퍼즐을넣을 리스트를 갱신한다.
    visited2 = [[False for _ in range(M)] for i in range(M)]
    getPuzzle(table, puzzle, visited2) # table에 퍼즐리스트를 갱신한다.
    print(empty)
    Emptymovelist = moveList(empty)
    puzzlemovelist = moveList(puzzle)
    print(Emptymovelist)
    print(puzzlemovelist)
    

solution(game_board, table)
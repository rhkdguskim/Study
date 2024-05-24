# https://school.programmers.co.kr/learn/courses/30/lessons/42894

# 검은색 블록을 놓을 수 있는 후보들을 탐색한다.
# 1행부터 N행까지 모두 탐색하면서 한번도 가로막히지않고 후보들까지 갈 수 있는지 계산한다.
# 갈수있다면 블록을 놓고, 갈 수 없다면 블록을 놓지 않는다.
# 블록을 놓았을때 직사각형이 만들어진다면 직사각형 파괴한다.
# 모두 다 순회했는데 블록을 놓을 수 없다면 종료.

# 1. 그래프를 탐색하여, 검은색 블록이 채워져야하는 조건을 구한다.
# 2. 

def solution(board):
    n = len(board)
    # 현재위치를 기준으로 높이 너비가 주어졌다면 자기자신이 아닌값이 검은색 블록이 채워져야한다.
    def make_block(y, x, h, w, number):
        block = set()
        start_h, end_h, h_cnt = 0, h, 1
        start_w , end_w, w_cnt = 0, w, 1
        
        for i in range(start_h, end_h, h_cnt):
            for j in range(start_w, end_w, w_cnt):
                ny, nx = i+y, j+x
                if board[ny][nx] != number:
                    block.add((ny, nx))
        
        return block
    
    def search(i, j, number, visited):
        block = []
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = []
        queue.append((i, j))
        block.append((i, j))
        visited[i][j] = True
        h, w = 0, 0
        min_j = j
        while queue:
            y, x = queue.pop()
            for dy, dx in moves:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and board[ny][nx] == number:
                    visited[ny][nx] = True
                    h += abs(dy)
                    w += abs(dx)
                    queue.append((ny, nx))
                    block.append((ny, nx))
                    min_j = min(min_j, nx)
        
        return [abs(h+1), abs(w+1), min_j, block]

    def break_block(x, black_blocks : dict, blocks : dict):
        cur_y = -1
        ret = False
        for i in range(n):
            if board[i][x] != 0:
                break
            
            cur_y = i
            
        if cur_y == -1:
            return False
        
        for key in black_blocks.keys():
            if (cur_y, x) in black_blocks[key] and key in blocks:
                black_blocks[key].remove((cur_y, x))
                blocks[key].append((cur_y, x))
                board[cur_y][x] = key
                ret = True

                if len(black_blocks[key]) == 0:
                    for b_y, b_x in blocks[key]:
                        board[b_y][b_x] = 0
                    
                    blocks.pop(key)
                        
        return ret
            
    
    v = [[False] * n for _ in range(n)]
    
    black_blocks = {}
    blocks = {}
    for i in range(n):
        for j in range(n):
            if not v[i][j] and board[i][j] != 0:
                number = board[i][j]
                h, w, min_j, b = search(i, j, number, v)
                black_blocks[number] = make_block(i, min_j, h, w, number)
                blocks[number] = b
    
    cnt = len(blocks)
    while True:
        is_end = False
        for i in range(n):
            is_end |= break_block(i, black_blocks, blocks)
        
        if is_end == False:
            break
        
    return cnt - len(blocks)

#print(solution([[0, 0, 0, 0, 0], [1, 0, 0, 2, 0], [1, 2, 2, 2, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]))
from collections import deque

def solution(places):
    PLAYER = 'P'
    TABLE = 'O'
    PARTITION = 'X'
    
    # BFS로 거리두기 체크
    def bfs(i, j, place):
        visited = [[False] * 5 for _ in range(5)]
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([(i, j, 0)])
        visited[i][j] = True
        
        while queue:
            y, x, dist = queue.popleft()
            if 1 <= dist <= 2 and place[y][x] == PLAYER:
                return False
            if dist == 2:
                continue
            
            for dy, dx in moves:
                ny, nx = y + dy, x + dx
                if 0 <= ny < 5 and 0 <= nx < 5 and not visited[ny][nx] and place[ny][nx] != PARTITION:
                    visited[ny][nx] = True
                    queue.append((ny, nx, dist + 1))
        
        return True
    
    answer = []
    for place in places:
        is_ok = True
        for i in range(5):
            if not is_ok:
                break
            for j in range(5):
                if place[i][j] == PLAYER:
                    if not bfs(i, j, place):
                        is_ok = False
                        break
                        
        answer.append(1 if is_ok else 0)
    
    return answer
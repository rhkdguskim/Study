from collections import deque
import sys

def solution(board, r, c):
    def bfs(start_y, start_x):
        # 이동 경로 및 거리를 계산하는 BFS 함수
        distance = [[sys.maxsize] * 4 for _ in range(4)]
        queue = deque([(start_y, start_x)])
        distance[start_y][start_x] = 0
        
        while queue:
            y, x = queue.popleft()
            
            # 상하좌우 이동 및 Ctrl 이동
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = y + dy, x + dx
                while 0 <= ny < 4 and 0 <= nx < 4:
                    if distance[ny][nx] > distance[y][x] + 1:
                        distance[ny][nx] = distance[y][x] + 1
                        queue.append((ny, nx))
                    if board[ny][nx] != 0:
                        break
                    ny += dy
                    nx += dx
                    
        return distance

    def get_min_moves(pos, cnt, path):
        # 백트래킹을 사용하여 최소 이동 횟수를 계산하는 함수
        if cnt == len(pairs):
            return 0
        
        min_moves = sys.maxsize
        for i, (first, second) in enumerate(pairs):
            if i not in path:
                path.add(i)
                # 첫 번째 카드 선택
                move1 = dist[pos][first[0]][first[1]] + 1
                # 두 번째 카드 선택
                move2 = dist[first][second[0]][second[1]] + 1
                # 두 카드를 제거하고 다음 카드로 이동
                result = move1 + move2 + get_min_moves(second, cnt + 1, path)
                min_moves = min(min_moves, result)
                path.remove(i)
        
        return min_moves

    # 카드 위치 파악
    card_positions = {}
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                if board[i][j] not in card_positions:
                    card_positions[board[i][j]] = []
                card_positions[board[i][j]].append((i, j))
    
    # 모든 카드 쌍의 위치 저장
    pairs = []
    for positions in card_positions.values():
        pairs.append(positions)
    
    # 모든 위치의 BFS 결과 저장
    dist = {}
    for i in range(4):
        for j in range(4):
            dist[(i, j)] = bfs(i, j)

    # 최소 이동 횟수 계산
    return get_min_moves((r, c), 0, set())

# 예시 입력
print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))

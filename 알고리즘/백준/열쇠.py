# https://www.acmicpc.net/problem/9328
# 상근이의 시작위치는 가장 가장자리에 있는 빈칸의 경우의 수이다.

# 상근이가 갈 수 있는 곳을 구한다. 
  # 문을 방문했을때 열쇠가 있다면 지나갈 수 있다.
  # 문을 방문했을때 열쇠가 없다면 지나갈 수 없다.
  # 키와 문서와 열수있는 문은 빈공간(.)으로 채워준다.

# 상근이가 갈 수 있는곳이 없다면 종료한다.
import sys
input = sys.stdin.readline


def start_pos():
    global ans
    start = []
    for i in range(h):
        for j in range(w):
            if (i == h-1 or i == 0 or j == w-1 or j == 0) and table[i][j] != '*':
                if table[i][j] == '.':
                    start.append((i, j))
                elif table[i][j].isalpha():
                    if table[i][j].islower():
                        key.setdefault(table[i][j].upper(), True)
                        start.append((i, j))
                        table[i][j] = '.'
                    else:
                        if table[i][j] in key:
                            table[i][j] = '.'
                            start.append((i, j))
                elif table[i][j] == '$':
                    table[i][j] = '.'
                    ans += 1
                    start.append((i, j))
    return start

def can_go(start):
    queue = []
    visited = [[False for _ in range(w)] for _ in range(h)]
    for i, j in start:
        queue.append((i, j))
        visited[i][j] = True
        
    get_key = False
    cnt = 0
    while queue:
        y, x = queue.pop()
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = dy + y, dx + x
            if h > ny >=0 and w > nx >=0 and not visited[ny][nx] and table[ny][nx] != '*':
                visited[ny][nx] = True
                if table[ny][nx].isalpha():
                    if table[ny][nx].isupper():
                        if table[ny][nx] in key:
                            table[ny][nx] = '.'
                            queue.append((ny, nx))
                    else:
                        get_key = True
                        key.setdefault(table[ny][nx].upper(), True)
                        table[ny][nx] = '.'
                        queue.append((ny, nx))
                else:
                    if table[ny][nx] != '*':
                        queue.append((ny, nx))
                        if table[ny][nx] == '$':
                            table[ny][nx] = '.'
                            cnt += 1
    return get_key, cnt
    

T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    table = [list(str(input().strip())) for _ in range(h)]
    already_key = str(input().strip())
    key = {}
    ans = 0
    
    for k in already_key:
        key.setdefault(k.upper(), True)
    
    while True:
        start = start_pos()
        get_key, cnt = can_go(start)
        #print(get_key, cnt, key)
        if not get_key and cnt == 0:
            break
        ans += cnt
        
    print(ans)
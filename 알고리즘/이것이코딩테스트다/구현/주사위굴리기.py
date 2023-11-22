#https://www.acmicpc.net/problem/14499
# 1. 주사위를 움직인다.
# 2. 주사위를 다 움직이면 주사위가 어떤 방향으로 이동했는지에 따라서 주사위의 상태를 바꿔준다. 주사위의 위치도 바꿔준다.
# 3. 주사위가 있는 위치의 바닥면이 0이면 바닥면에 주사위의 바닥값을 업데이트한다. 바닥면이 0이 아니면 바닥면의값을 주사위의 바닥면의 값으로 업데이트한다.
# 4. 주사위의 위의 값을 출력한다.
# 5. 명령의 개수가 끝날때까지 1,2,3을 반복한다.

move = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]
class Dice():
    def __init__(self):
        self.top = 0
        self.bottom = 0
        self.north = 0
        self.south = 0
        self.west = 0
        self.east = 0
    
    def North(self):
        top = self.top
        bottom = self.bottom
        north = self.north
        south = self.south
        
        self.bottom = north
        self.north = top
        self.top = south
        self.south = bottom
        
    def South(self):
        top = self.top
        bottom = self.bottom
        north = self.north
        south = self.south
        
        self.bottom = south
        self.south = top
        self.top = north
        self.north = bottom
    
    def West(self):
        top = self.top
        bottom = self.bottom
        west = self.west
        east = self.east
        
        self.bottom = east
        self.east = top
        self.top = west
        self.west = bottom
    
    
    def East(self):
        top = self.top
        bottom = self.bottom
        west = self.west
        east = self.east
        
        self.bottom = west
        self.west = top
        self.top = east
        self.east = bottom
    
    
N, M, x, y, cnt = map(int, input().split())
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))
    
command = list(map(int, input().split()))
mydice = Dice()

for cmd in command:
    i,j = move[cmd]
    dx = i+x
    dy = j+y
    
    if N > dx >= 0 and M > dy >= 0:
        if cmd == 1:
            mydice.East()
        elif cmd == 2:
            mydice.West()
        elif cmd == 3:
            mydice.North()
        else:
            mydice.South()
        
        x = dx
        y = dy
        print(mydice.top)
        
        if table[x][y] == 0:
            table[x][y] = mydice.bottom
        else:
            mydice.bottom = table[x][y]
            table[x][y] = 0
        
        
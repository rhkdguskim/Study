# https://www.acmicpc.net/problem/13460
from copy import deepcopy
from collections import deque
N , M = map(int, input().split()) # 세로, 가로

table = []
red = [0,0]
blue = [0,0]
for i in range(N):
    char = input()
    for j in range(len(char)):
        if char[j] == 'R':
            red = [i,j]
        elif char[j] == 'B':
            blue = [i,j]
    table.append(list(char))
    
    
def left(table, red, blue):
    redFlag = False
    blueFlag = False
    red_y ,red_x = red
    blue_y, blue_x = blue
    
    if red_x < blue_x: # 레드가 x좌표가 더 작으면 레드먼저 이동
        # 레드 이동
        for i in range(red_x - 1, -1, -1): # 현재위치부터 다음위치까지
            if table[red_y][i] == '.': # 빈칸이면 이동
                table[red_y][red[1]] = '.' # 자기자신을 빈칸으로 설정
                table[red_y][i] = 'R'
                red[1] = i
            elif table[red_y][i] == '#': # 벽이면 탐색중지
                break
            elif table[red_y][i] == '0': # 0이면 Goal
                table[red_y][red[1]] = '.'
                redFlag = True
                break
            else : # 블루를 만난경우
                break
            
        # 블루 이동
        for i in range(blue_x - 1, -1, -1): # 현재위치부터 다음위치까지
            if table[blue_y][i] == '.': # 빈칸이면 이동
                table[blue_y][blue[1]] = '.' # 자기자신을 빈칸으로 설정
                table[blue_y][i] = 'B'
                blue[1] = i
            elif table[blue_y][i] == '#': # 벽이면 탐색중지
                break
            elif table[blue_y][i] == '0': # 0이면 Goal
                table[blue_y][blue[1]] = '.'
                blueFlag = True
                break
            else: # 레드를 만난경우
                break
        else:
            # 블루 이동
            for i in range(blue_x - 1, -1, -1): # 현재위치부터 다음위치까지
                if table[blue_y][i] == '.': # 빈칸이면 이동
                    table[blue_y][blue[1]] = '.' # 자기자신을 빈칸으로 설정
                    table[blue_y][i] = 'B'
                    blue[1] = i
                elif table[blue_y][i] == '#': # 벽이면 탐색중지
                    break
                elif table[blue_y][i] == '0': # 0이면 Goal
                    table[blue_y][blue[1]] = '.'
                    blueFlag = True
                    break
                else: # 레드를 만난경우
                    break
                
            # 레드 이동
            for i in range(red_x - 1, -1, -1): # 현재위치부터 다음위치까지
                if table[red_y][i] == '.': # 빈칸이면 이동
                    table[red_y][red[1]] = '.' # 자기자신을 빈칸으로 설정
                    table[red_y][i] = 'R'
                    red[1] = i
                elif table[red_y][i] == '#': # 벽이면 탐색중지
                    break
                elif table[red_y][i] == '0': # 0이면 Goal
                    table[red_y][red[1]] = '.'
                    redFlag = True
                    break
                else : # 블루를 만난경우
                    break
            
    return red, blue, redFlag, blueFlag, table

def right(table, red, blue):
    redFlag = False
    blueFlag = False
    red_y ,red_x = red
    blue_y, blue_x = blue
    
    if red_x > blue_x: # 레드가 x좌표가 더 크면 레드먼저 이동
        # 레드 이동
        for i in range(red_x + 1, M): # 현재위치부터 다음위치까지
            if table[red_y][i] == '.': # 빈칸이면 이동
                table[red_y][red[1]] = '.' # 자기자신을 빈칸으로 설정
                table[red_y][i] = 'R'
                red[1] = i
            elif table[red_y][i] == '#': # 벽이면 탐색중지
                break
            elif table[red_y][i] == '0': # 0이면 Goal
                table[red_y][red[1]] = '.'
                redFlag = True
                break
            else : # 블루를 만난경우
                break
            
        # 블루 이동
        for i in range(blue_x + 1, M): # 현재위치부터 다음위치까지
            if table[blue_y][i] == '.': # 빈칸이면 이동
                table[blue_y][blue[1]] = '.' # 자기자신을 빈칸으로 설정
                table[blue_y][i] = 'B'
                blue[1] = i
            elif table[blue_y][i] == '#': # 벽이면 탐색중지
                break
            elif table[blue_y][i] == '0': # 0이면 Goal
                table[blue_y][blue[1]] = '.'
                blueFlag = True
                break
            else: # 레드를 만난경우
                break
        else:
            # 블루 이동
            for i in range(blue_x + 1, M): # 현재위치부터 다음위치까지
                if table[blue_y][i] == '.': # 빈칸이면 이동
                    table[blue_y][blue[1]] = '.' # 자기자신을 빈칸으로 설정
                    table[blue_y][i] = 'B'
                    blue[1] = i
                elif table[blue_y][i] == '#': # 벽이면 탐색중지
                    break
                elif table[blue_y][i] == '0': # 0이면 Goal
                    table[blue_y][blue[1]] = '.'
                    blueFlag = True
                    break
                else: # 레드를 만난경우
                    break
                
            # 레드 이동
            for i in range(red_x + 1, M): # 현재위치부터 다음위치까지
                if table[red_y][i] == '.': # 빈칸이면 이동
                    table[red_y][red[1]] = '.' # 자기자신을 빈칸으로 설정
                    table[red_y][i] = 'R'
                    red[1] = i
                elif table[red_y][i] == '#': # 벽이면 탐색중지
                    break
                elif table[red_y][i] == '0': # 0이면 Goal
                    table[red_y][red[1]] = '.'
                    redFlag = True
                    break
                else : # 블루를 만난경우
                    break
            
    return red, blue, redFlag, blueFlag, table

def up(table, red, blue):
    redFlag = False
    blueFlag = False
    red_y ,red_x = red
    blue_y, blue_x = blue
    
    if red_y < blue_y: # 레드가 y좌표가 더 작으면 레드먼저 이동
        # 레드 이동
        for i in range(red_y - 1, -1, -1): # 현재위치부터 다음위치까지
            if table[i][red_x] == '.': # 빈칸이면 이동
                table[red[0]][red_x] = '.' # 자기자신을 빈칸으로 설정
                table[i][red_x] = 'R'
                red[0] = i
            elif table[i][red_x] == '#': # 벽이면 탐색중지
                break
            elif table[i][red_x] == '0': # 0이면 Goal
                table[red[0]][red_x] = '.'
                redFlag = True
                break
            else : # 블루를 만난경우
                break
            
        # 블루 이동
        for i in range(blue_y -1, -1, -1): # 현재위치부터 다음위치까지
            if table[i][blue_x] == '.': # 빈칸이면 이동
                table[blue[0]][blue_x] = '.' # 자기자신을 빈칸으로 설정
                table[i][blue_x] = 'B'
                blue[0] = i
            elif table[i][blue_x] == '#': # 벽이면 탐색중지
                break
            elif table[i][blue_x] == '0': # 0이면 Goal
                table[blue[0]][blue_x] = '.'
                blueFlag = True
                break
            else: # 레드를 만난경우
                break
        else:
            # 블루 이동
            for i in range(blue_y -1, -1, -1): # 현재위치부터 다음위치까지
                if table[i][blue_x] == '.': # 빈칸이면 이동
                    table[blue[0]][blue_x] = '.' # 자기자신을 빈칸으로 설정
                    table[i][blue_x] = 'B'
                    blue[0] = i
                elif table[i][blue_x] == '#': # 벽이면 탐색중지
                    break
                elif table[i][blue_x] == '0': # 0이면 Goal
                    table[blue[0]][blue_x] = '.'
                    blueFlag = True
                    break
                else: # 레드를 만난경우
                    break
                
            # 레드 이동
            for i in range(red_y - 1, -1, -1): # 현재위치부터 다음위치까지
                if table[i][red_x] == '.': # 빈칸이면 이동
                    table[red[0]][red_x] = '.' # 자기자신을 빈칸으로 설정
                    table[i][red_x] = 'R'
                    red[0] = i
                elif table[i][red_x] == '#': # 벽이면 탐색중지
                    break
                elif table[i][red_x] == '0': # 0이면 Goal
                    table[red[0]][red_x] = '.'
                    redFlag = True
                    break
                else : # 블루를 만난경우
                    break
            
    return red, blue, redFlag, blueFlag, table

def down(table, red, blue):
    redFlag = False
    blueFlag = False
    red_y ,red_x = red
    blue_y, blue_x = blue
    
    if red_y > blue_y: # 레드가 y좌표가 더 크면 레드먼저 이동
        # 레드 이동
        for i in range(red_y + 1, N): # 현재위치부터 다음위치까지
            if table[i][red_x] == '.': # 빈칸이면 이동
                table[red[0]][red_x] = '.' # 자기자신을 빈칸으로 설정
                table[i][red_x] = 'R'
                red[0] = i
            elif table[i][red_x] == '#': # 벽이면 탐색중지
                break
            elif table[i][red_x] == '0': # 0이면 Goal
                table[red[0]][red_x] = '.'
                redFlag = True
                break
            else : # 블루를 만난경우
                break
            
        # 블루 이동
        for i in range(blue_y + 1, N): # 현재위치부터 다음위치까지
            if table[i][blue_x] == '.': # 빈칸이면 이동
                table[blue[0]][blue_x] = '.' # 자기자신을 빈칸으로 설정
                table[i][blue_x] = 'B'
                blue[0] = i
            elif table[i][blue_x] == '#': # 벽이면 탐색중지
                break
            elif table[i][blue_x] == '0': # 0이면 Goal
                table[blue[0]][blue_x] = '.'
                blueFlag = True
                break
            else: # 레드를 만난경우
                break
        else:
            # 블루 이동
            for i in range(blue_y +1 , N): # 현재위치부터 다음위치까지
                if table[i][blue_x] == '.': # 빈칸이면 이동
                    table[blue[0]][blue_x] = '.' # 자기자신을 빈칸으로 설정
                    table[i][blue_x] = 'B'
                    blue[0] = i
                elif table[i][blue_x] == '#': # 벽이면 탐색중지
                    break
                elif table[i][blue_x] == '0': # 0이면 Goal
                    table[blue[0]][blue_x] = '.'
                    blueFlag = True
                    break
                else: # 레드를 만난경우
                    break
                
            # 레드 이동
            for i in range(red_y +1, N): # 현재위치부터 다음위치까지
                if table[i][red_x] == '.': # 빈칸이면 이동
                    table[red[0]][red_x] = '.' # 자기자신을 빈칸으로 설정
                    table[i][red_x] = 'R'
                    red[0] = i
                elif table[i][red_x] == '#': # 벽이면 탐색중지
                    break
                elif table[i][red_x] == '0': # 0이면 Goal
                    table[red[0]][red_x] = '.'
                    redFlag = True
                    break
                else : # 블루를 만난경우
                    break
            
    return red, blue, redFlag, blueFlag, table

def move(table, red, blue, pos):
    if pos == 0:
        return left(table,red,blue)
    elif pos == 1:
        return right(table,red,blue)
    elif pos == 2:
        return up(table,red,blue)
    else :
        return down(table,red,blue)

def start(table, red, blue):
    queue = deque([(table, red, blue, 0)])
    visited = set((tuple(red), tuple(blue)))

    while queue:
        table, red, blue, depth = queue.popleft()

        if depth == 10:
            break

        for i in range(4):
            newred, newblue, flag1, flag2, newtable = move(deepcopy(table), deepcopy(red), deepcopy(blue), i)

            if not flag2 and flag1:
                return depth + 1

            if (tuple(newred), tuple(newblue)) not in visited:
                visited.add((tuple(newred), tuple(newblue)))
                queue.append((newtable, newred, newblue, depth + 1))

    return -1


result = start(table, red, blue)
print(result)
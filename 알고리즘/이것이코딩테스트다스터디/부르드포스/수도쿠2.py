# https://www.acmicpc.net/problem/2580
table = []

for i in range(9):
    new = list(map(int, input().split()))
    table.append(new)
    
def get_vailed(table):
    for row in range(9):
        for col in range(9):
            if table[row][col] == 0:
                return row, col
    
    return None
    
def is_vailed(col, row , num):
    
    for k in range(9):
        if table[col][k] == num:
            return False
    
    for k in range(9):
        if table[k][row] == num:
            return False
        
    newcol = (col//3) * 3
    newrow = (row//3) * 3
    
    for k in range(3):
        for n in range(3):
            if table[k+newcol][n+newrow] == num:
                return False
            
    return True

def sudoku(table):
    if not get_vailed(table): # 모든 스도쿠가 꽉 차면
        return True
    
    col, row = get_vailed(table)
    
    for num in range(1,10):
        if is_vailed(col,row, num):
            table[col][row] = num # 숫자를 넣어본다.
            
            if sudoku(table):
                return True

            table[col][row] = 0 # 넣은 숫자를 뺀다.


                
sudoku(table)

for i in range(len(table)):
    print(*table[i])

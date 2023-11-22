# https://school.programmers.co.kr/learn/courses/30/lessons/150366

MAX_SIZE = 50
table = [[[] for _ in range(MAX_SIZE)] for _ in range(MAX_SIZE)]

for r in range(MAX_SIZE):
    for c in range(MAX_SIZE):
        table[r][c].append('EMPTY')
        table[r][c].append(set())
        table[r][c][1].add(((r, c)))

def update(r, c, value):
    for g_r, g_c in table[r][c][1]:
        table[g_r][g_c][0] = value
        
def update_all(value1, value2):
    for r in range(MAX_SIZE):
        for c in range(MAX_SIZE):
            if table[r][c][0] == value1:
                table[r][c][0] = value2
                
def merge(r1, c1, r2, c2):
    if table[r1][c1][1] == table[r2][c2][1]:
        return
    
    unioned_table = table[r1][c1][1] | table[r2][c2][1]
    
    for g_r, g_c in table[r1][c1][1]:
        table[g_r][g_c][1] = unioned_table
        
    for g_r, g_c in table[r2][c2][1]:
        table[g_r][g_c][1] = unioned_table
        
    
    if table[r1][c1][0] == 'EMPTY':
        for g_r, g_c in table[r1][c1][1]:
            table[g_r][g_c][0] =  table[r2][c2][0]
    else:
        for g_r, g_c in table[r2][c2][1]:
            table[g_r][g_c][0] =  table[r1][c1][0]
            
def unmerge(r1, c1):
    for g_r, g_c in table[r1][c1][1]:
        if (g_r, g_c) != (r1, c1):
            table[g_r][g_c][1] = set()
            table[g_r][g_c][1].add(((g_r, g_c)))
            table[g_r][g_c][0] = 'EMPTY'
    
    table[r1][c1][1] = set()
    table[r1][c1][1].add(((r1, c1)))
    
def cmd_print(r1, c1):
    return table[r1][c1][0]


def solution(commands):
    answer = []
    for command in commands:
        command = command.split(' ')
        
        if command[0] == 'UPDATE':
            if len(command) == 4:
                r1, c1, value = command[1], command[2], command[3]
                r1, c1 = int(r1)-1, int(c1) -1
                update(r1, c1, value)
            else:
                value1, value2 = command[1], command[2]
                update_all(value1, value2)
        elif command[0] == 'MERGE':
            r1, c1, r2, c2 = command[1], command[2], command[3], command[4]
            r1, c1, r2, c2 = int(r1)-1, int(c1) -1, int(r2)-1, int(c2) -1
            merge(r1, c1, r2 ,c2)
        elif command[0] == 'UNMERGE':
            r1, c1 = command[1], command[2]
            r1, c1 = int(r1)-1, int(c1) -1
            unmerge(r1, c1)
        elif command[0] == 'PRINT':
            r1, c1 = command[1], command[2]
            r1, c1 = int(r1)-1, int(c1) -1
            answer.append(cmd_print(r1, c1))
            
    return answer

#commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
commands = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
print(solution(commands))
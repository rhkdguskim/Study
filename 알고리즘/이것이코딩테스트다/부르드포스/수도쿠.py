# https://www.acmicpc.net/problem/2580
from collections import deque
table = []
emptynumberlist = deque()

for i in range(9):
    new = list(map(int, input().split()))
    for j in range(9):
        if new[j] == 0:
            emptynumberlist.append([i,j]) # i,j 의 좌표를 넣는다.
    table.append(new)
    
def getPos(i,j):
    if 3 >i >=0 and 3>j>=0: #첫번째
        return [[0,3],[0,3]]        
    elif 3 > i >=0 and 6>j>=3: # 두번째
        return [[0,3],[3,6]]
    elif 3 > i >= 0 and 9>j>=6: # 세번째
        return [[0,3],[6,9]]
    elif 6 >i >=3 and 3>j>=0: # 4번째
        return [[3,6],[0,3]]
    elif 6 > i >=3 and 6>j>=3: # 5번째
        return [[3,6],[3,6]]
    elif 6 > i >= 3 and 9>j>=6: # 6번째
        return [[3,6],[6,9]]
    elif 9 >i >=6 and 3>j>=0: #7번째
        return [[6,9],[0,3]]
    elif 9 > i >=6 and 6>j>=3: # 8번째
        return [[6,9],[3,6]]
    elif 9 > i >= 6 and 9>j>=6: # 9번째
        return [[6,9],[6,9]]

def isvailed(i,j):
    mynum = {1,2,3,4,5,6,7,8,9}
    y , x = getPos(i,j)
    
    for k in range(9):
        if table[i][k] in mynum:
            mynum.remove(table[i][k])
            
    if len(mynum) == 1:
        table[i][j] = mynum.pop()
        return True
        
    for k in range(9):
        if table[k][j] in mynum:
            mynum.remove(table[k][j])
            
    if len(mynum) == 1:
        table[i][j] = mynum.pop()
        return True
            
    for k in range(y[0],y[1]):
        for n in range(x[0],x[1]):
            if table[k][n] in mynum:
                mynum.remove(table[k][n])
        
    if len(mynum) == 1:
        table[i][j] = mynum.pop()
        return True
    
    return False
    

while emptynumberlist:
    i,j = emptynumberlist.popleft()
    
    if not isvailed(i,j):
        emptynumberlist.append([i,j])

for t in range(len(table)):
    print(*table[t])



# https://www.acmicpc.net/problem/16234
N, L, R = map(int, input().split())

table = []
move = [(1,0), (-1,0), (0,1), (0,-1)]
for _ in range(N):
    table.append(list(map(int, input().split())))

def unionCountry(i,j, table, visited):
    unionGroup = []
    if visited[i][j]:
        return unionGroup
    
    queue = [(i,j)]
    visited[i][j] = True
    unionGroup.append((i,j))
    while queue:
        y, x = queue.pop()
        for v,w in move:
            dy = y+v
            dx = x+w
            if N > dy >=0 and N > dx >=0 and not visited[dy][dx]:
                if R >= abs(table[dy][dx]-table[y][x]) >= L:
                    visited[dy][dx] = True
                    queue.append((dy,dx))
                    unionGroup.append((dy,dx))
                
    return unionGroup

def unionCountryGroup(table):
    visited = [[False for _ in range(N)] for _ in range(N)]
    unionCountryGroupList = []
    for i in range(N):
        for j in range(N):
            group = unionCountry(i,j,table, visited)
            if group and len(group)>1:
                unionCountryGroupList.append(group)
                
    return unionCountryGroupList

def updateContryTable(unionCountryGroupList, table):
    for contryGroup in unionCountryGroupList:
        peoplesum = 0
        for i,j in contryGroup:
            peoplesum += table[i][j]
            
        result = peoplesum // len(contryGroup)
        
        for i,j in contryGroup:
            table[i][j] = result

unioncontrylist = unionCountryGroup(table)
if not unioncontrylist:
    print(0)
else:
    time = 0
    while unioncontrylist:
        updateContryTable(unioncontrylist, table)
        unioncontrylist = unionCountryGroup(table)
        time += 1
    print(time)
        
# https://www.acmicpc.net/problem/2239
def getavailable(i, j):
    h, w = getpos(i,j)
    temp = {1,2,3,4,5,6,7,8,9}

    for k in range(h, h+3):
        for n in range(w, w+3):
            if table[k][n] in temp:
                temp.remove(table[k][n])

    for t in range(9):
        n1 = table[i][t]
        n2 = table[t][j]
        if n1 in temp:
            temp.remove(n1)

        if n2 in temp:
            temp.remove(n2)

    return temp

def getpos(i, j):
    h, w = 0, 0
    if 3 > i >= 0:
        h = 0
    elif 6 > i >= 3:
        h = 3
    elif 9 > i >= 6:
        h = 6

    if 3 > j >= 0:
        w = 0
    elif 6 > j >= 3:
        w = 3
    elif 9 > j >= 6:
        w = 6

    return h, w

table = [[0 for _ in range(9)] for _ in range(9)]

cnt = 0
for i in range(9):
    temp = list(input())
    for j in range(len(temp)):
        num = int(temp[j])
        if num == 0:
            cnt += 1
        table[i][j] = num


def dfs(index, depth):
    global end
    if end:
        return
    if depth == cnt:
        for result in table:
            char = ''
            for a in result:
                char += str(a)
            end = True
            print(char)
        return
    
    y = index // 9
    x = index % 9

    if table[y][x] == 0:
        nums = getavailable(y,x)
        if not nums:
            return

        for n in nums:
            table[y][x] = n
            dfs(index +1, depth+1)
            table[y][x] = 0
    else:
        dfs(index+1, depth)

end = False
dfs(0,0)
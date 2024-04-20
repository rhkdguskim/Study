N , M = map(int, input().split())

def dfs(i, numlist):
    if len(numlist) == M:
        for i in range(len(numlist)):
            if i == len(numlist) -1:
                print(numlist[i])
            else:
                print(numlist[i], end=' ')
        return
    
    for k in range(1, N+1):
        if k >= numlist[-1]:
            numlist.append(k)
            dfs(k, numlist)
            numlist.pop()

numlist = []     
for i in range(1, N+1):
    numlist.append(i)
    dfs(i, numlist)
    numlist.pop()
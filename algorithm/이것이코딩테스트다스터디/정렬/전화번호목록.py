# https://www.acmicpc.net/problem/5052
t = int(input())

arr = [[] for _ in range(t)]
for i in range(t):
    n = int(input())
    for _ in range(n):
        arr[i].append(str(input()))

for i in range(t):
    findprefix = False
    for j in range(len(arr[i])):
        for k in range(j+1, len(arr[i])):
            if len(arr[i][j]) < len(arr[i][k]):
                if arr[i][j] in arr[i][k]:
                    findprefix = True
                    print("NO")
                    break
                
        if findprefix:
            break
    if not findprefix:
        print("YES")
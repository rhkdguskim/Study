N, W = map(int, input().split())

w = []
v = []
for _ in range(N):
    a ,b  = map(int, input().split())
    w.append(a) # 무게 배열
    v.append(b) # 가치 배열

dy = [[0 for _ in range(W+1)] for _ in range(len(v)+1)]

for i in range(1, len(v)+1): # 아이템
    for j in range(1, W+1): # 무게
        if(w[i-1] > j):
            dy[i][j] = dy[i-1][j]
        else :
            dy[i][j] = max(dy[i-1][j-w[i-1]] + v[i-1], dy[i-1][j]) # 추가하지 않은경우, 자기자신을빼고 물품을 추가한경우 중에서 Max 값을 선택한다.
            
print(dy[len(v)][W])
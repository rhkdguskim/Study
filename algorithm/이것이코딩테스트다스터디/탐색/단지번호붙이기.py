# <그림1>과 같이 정사각형 모양의 지도가 있다.
# 1은 집이 있는곳 0은 집이 없는곳이다.
# 철수는 이 지도를 가지고 연결된 모임인 단지를 정의하고 단지에 번호를 붙히려고 한다.
# 여기서 연결되어있다는것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는경우를 말한다. ( 대각선에 있는경우 집이 아님)
# 지도를 입력하여 단지수를 출력하고, 단지에 속하는 집을 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int , input())))

visited = [[False] * N for _ in range(N)]
count = 0
group = []
def dfs(i, j, count):
    
    if (not visited[i][j]) and arr[i][j] == 1:
        group.append(count)
        visited[i][j] = True
        if(N > i+1 >= 0):
            dfs(i+1,j, count)
        if(N > i-1 >= 0):
            dfs(i-1,j, count)
        if(N > j+1 >= 0):
            dfs(i,j+1, count)
        if(N > j-1 >= 0):
            dfs(i,j-1, count)
    else :
        return False
    
    return True

for i in range(N):
    for j in range(N):
        if(dfs(i,j,count) == True):
            count += 1
            
print(count)
newarr = []
for i in range(count):
    newarr.append(group.count(i))

newarr.sort()
for data in newarr:
    print(data)
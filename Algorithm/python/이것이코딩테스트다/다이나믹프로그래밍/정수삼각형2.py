# https://www.acmicpc.net/problem/1932
# 탑다운 방식
n = int(input()) # 삼각형의 크기
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

dp = [[0 for _ in range(n+1)]for _ in range(n)]
dp[0][0] = triangle[0][0]

for i in range(1, len(triangle)):
    for j in range(len(triangle[i])):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            
print(max(dp[n-1]))


# 바텀업 방식
n = int(input()) # 삼각형의 크기
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))
    
for i in range(len(triangle)-1, 0, -1):
    for j in range(len(triangle[i])-1):
        triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])
        
print(triangle[0][0])
# https://www.acmicpc.net/problem/2096

N = int(input())

current = [[0,0] for _ in range(3)] # maxValue, minValue

for _ in range(N):
    a,b,c = map(int, input().split())
    # 최대값 구하기
    temp = [0 for _ in range(3)]
    temp[0] = a + max(current[0][0], current[1][0]) # 첫번째 수
    temp[1] = b + max(current[0][0], current[1][0], current[2][0]) # 두번째 수
    temp[2] = c + max(current[1][0], current[2][0]) # 세번째 수
    
    for i in range(len(temp)):
        current[i][0] = temp[i]
    
    # 최소갑 구하기
    temp[0] = a + min(current[0][1], current[1][1]) # 첫번째 수
    temp[1] = b + min(current[0][1], current[1][1], current[2][1]) # 두번째 수
    temp[2] = c + min(current[1][1], current[2][1]) # 세번째 수
    
    for i in range(len(temp)):
        current[i][1] = temp[i]
    
print(max(current[0][0], current[1][0], current[2][0]), end=' ')
print(min(current[0][1], current[1][1], current[2][1]))
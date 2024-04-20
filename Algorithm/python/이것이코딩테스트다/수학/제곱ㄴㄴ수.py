# https://www.acmicpc.net/problem/1016
min, max = map(int, input().split())
visited = [1] * (max - min + 1) # 최대 1,000,000

i = 2
while i*i <= max:
    temp = min//(i*i) # i*i 으로 나눌수 있는 최소값을 찾는다.
    if min%(i*i) != 0: # 만약 소숫점이 생긴다면 1을 추가해준다.
        temp += 1

    while temp *i*i <= max: # 에라토스테네스의 체 처럼 나누어지는수를 초기화 해준다.
        print(temp * i*i - min, i, temp)
        if visited[temp * i*i - min]:
            visited[temp * i*i - min] = 0
                
        temp += 1
    i += 1

print(visited.count(1))
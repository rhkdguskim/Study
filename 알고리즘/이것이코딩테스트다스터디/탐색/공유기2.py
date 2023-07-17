# https://www.acmicpc.net/problem/2110
N, C = map(int, input().split())

house = []
for _ in range(N):
    house.append(int(input()))
    
house.sort() # 이분탐색을 위한 정렬


start = 1
end = house[-1] - house[0]

result = 0
if C == 2:
    print(house[-1] - house[0])
else:
    while start < end:
        mid = (start + end) // 2 # 거리
        router = house[0] # 제일 왼쪽에 있는집에 공유기를 설치한다.
        count = 1
        for i in range(len(house)):
            if house[i] - router  >= mid: # 공유기 설치 가능
                count += 1
                router = house[i]
        
        if count >= C: # 거리를 더 넓게 가져가본다.
            result = mid
            start = mid + 1
        else:
            end = mid # 거리를 더 짧게 가져가본다.
            
    print(result)
            
            
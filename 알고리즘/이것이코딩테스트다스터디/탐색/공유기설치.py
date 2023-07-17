# https://www.acmicpc.net/problem/2110
n, c = map(int, input().split())
house = list(map(int, input().split()))
house.sort()
start = 1
end = house[n-1] - house[0]

result = 0
if c == 2:
    print(house[n-1] - house[0])
else:
    while start < end:
        mid = (start + end) // 2
        router = house[0]
        count = 1
        for i in range(n):
            if house[i] - router >= mid:
                count += 1
                router = house[i]
            
        if count >= c:
            result = mid
            start = mid +1
        elif count < c:
            end = mid
            
    print(result)
            
    
    
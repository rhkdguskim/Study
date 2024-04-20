#https://www.acmicpc.net/problem/14501
N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int,input().split()))) # 0이 day 1이 value
    

def sol(day, value):
    if day >= N:
        if day == N:
            return value
        else:
            return 0
    
    result = max(sol(day + arr[day][0], value + arr[day][1]), sol(day+1, value))
    
    return result

print(sol(0,0))
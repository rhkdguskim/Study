# https://www.acmicpc.net/problem/5052
T = int(input())
for test_case in range(T):
    n = int(input())
    arr = sorted([input() for _ in range(n)])
    for i in range(n-1):
        if arr[i] == arr[i+1][:len(arr[i])]:
            print("NO")
            break
    else:
        print("YES")
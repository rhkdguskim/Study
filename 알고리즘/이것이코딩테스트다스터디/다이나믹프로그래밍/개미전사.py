N = int(input())
arr = list(map(int, input().split()))

for i in range(3, N):
    arr[i]= max(arr[i-2] + arr[i], arr[i-1])
    
print(arr[N-1])
import sys
input = sys.stdin.readline

def gcd(a, b):
    if b > a:
        a, b = b, a
        
    if b == 0: return 0
    
    while b != 0:
        tmp = a
        a = b
        b = tmp % b
    return a

def divisors(n):
    arr = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            arr.append(i)
            if i != n // i:
                arr.append(n // i)
    return sorted(arr)

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
    
arr.sort()
g = arr[1] - arr[0]

for i in range(1, N-1):
    dif = arr[i+1] - arr[i]
    g = gcd(g, dif)


ans = divisors(g)
ans.append(g)
print(' '.join(map(str, ans)))
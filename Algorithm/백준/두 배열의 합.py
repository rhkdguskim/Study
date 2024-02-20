# https://www.acmicpc.net/problem/2143

# A의 배열을 이중 순회하며 부분배열을 만든다. ( 누적합 )
# B 배열에서 부분배열중에 누적합과 더해서 T가 되는경우를 찾아야한다.
import sys
input = sys.stdin.readline

T = int(input())
n = int(input())

A = [0]*n


for i, a in enumerate(list(map(int, input().split()))):
    if i == 0:
        A[i] = a
    else:
        A[i] = A[i-1] + a
    
m = int(input())
B = [0]*m

def prefix_sum(arr, s, e):
    if s-1 > 0:
        return arr[e] - arr[s-1]
    else:
        return arr[e]

for i, b in enumerate(list(map(int, input().split()))):
    if i == 0:
        B[i] = b
    else:
        B[i] = B[i-1] + b

ans = 0
for i in range(n):
    for j in range(i, n):
        a_prefix = prefix_sum(A, i, j)
        for k in range(m):
            start = k
            end = m-1
            while end>=start:
                mid = (start+end)//2
                b_prefix = prefix_sum(B, k, mid)
                cost = a_prefix + b_prefix
                if cost == T:
                    print("A", i+1, j+1, "B", k+1, mid+1)
                    ans += 1
                    break
                elif T > cost:
                    start = mid + 1
                else:
                    end = mid - 1
                    
print(ans)
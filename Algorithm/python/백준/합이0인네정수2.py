from bisect import bisect_left
from bisect import bisect_right

import sys
input = sys.stdin.readline


N = int(input())  # 배열의 크기
A, B, C, D = [], [], [], []

for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    
AB = []
CD = []
for i in range(N):
    for j in range(N):
        AB.append(A[i]+B[j])
        CD.append(C[i]+D[j])
        

left = 0
right = len(CD) -1
ans = 0
AB.sort()
CD.sort()

while left < len(AB) and right >= 0:
    cost = AB[left] + CD[right]
    # 0보다 클경우 right를 감소시킨다.
    if cost > 0:
        right -= 1
    # 0보다 작을경우 left를 증가시킨다.
    elif cost < 0:
        left += 1
    else:
        # 해당값이 몇개 있는지 카운팅한다.
        ab_new_l, ab_new_r = bisect_left(AB, AB[left]), bisect_right(AB, AB[left])
        cd_new_l, cd_new_r = bisect_left(CD, CD[right]), bisect_right(CD, CD[right])
        ans += (ab_new_r-ab_new_l) * (cd_new_r - cd_new_l)
        left = ab_new_r
        right = cd_new_l - 1
        
print(ans)
# https://www.acmicpc.net/problem/2812
# 맨앞에 숫자들이 작은숫자들이 있다면 이숫자들을 중에서 제일 작은값을 최대 K개 삭제한다.
import sys
N,K = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().strip()))

result = []
delNum = K

for i in range(N):
    while delNum>0 and result:
        if result[len(result)-1] < nums[i]:
            result.pop()
            delNum-=1
        else:
            break
    result.append(nums[i])
    
for i in range(N-K):
    print(result[i],end="")
# 10 4
# 4177252841
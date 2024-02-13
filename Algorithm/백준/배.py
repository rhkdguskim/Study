# https://www.acmicpc.net/problem/1092
# 가장 작은 무게를 들을 수 있는 크레인이, 가장 작은 무게의 박스를 찾아서 옮긴다.
# 가장 작은 무겔르 들을 수 있는 크레인이 가장 작은 무게를 들을 수 없는경우는 다음부터, 무게를 실을 수 없다.

# 크레인은 자기가 들을 수 있는 최대 무게를 항상 뽑는다. Mlog(M)
# 상자를 가장 무거운순으로 내림차순 정렬
# 크레인도 가장 무거운 순으로 내림차순 정렬
# 만약 상자의 첫번째가, 첫번재 크레인보다 클경우, 나를 수 없는경우의 수
import sys
input = sys.stdin.readline

N = int(input()) # 크레인의 수

cranes = list(map(int, input().split()))
M = int(input()) # 박스의 수
boxs_weight = list(map(int, input().split()))

cranes.sort(reverse=True)
boxs_weight.sort(reverse=True)

if cranes[0] < boxs_weight[0]: # 가장 무거운 박스가 크레인이 나를수 있는 무게보다 무거운경우
    print(-1)
else:
    time = 0
    while boxs_weight:
        for crain in cranes:
            for weight in boxs_weight:
                if crain >= weight:
                    boxs_weight.remove(weight)
                    break
                    
        time += 1
        
    print(time)
    

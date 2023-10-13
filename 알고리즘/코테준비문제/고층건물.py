# https://www.acmicpc.net/problem/1027
import sys
si = sys.stdin.readline

N = int(si())
arr = [0] + list(map(int, si().split()))

# 해당 빌딩으로부터 시작해서 왼쪽 오른쪽 둘다 가보면서 갈수있는 곳을 구한다.

for cur in range(1, N+1):
    # 각빌딩을 순회한다.
    
    # 자기자신의 바로 옆
    right = cur+1
    # 오른쪽을 탐색해본다
    building = []
    while right > N:
        if building:
            if building[-1] > arr[cur]: # 자기자신보다 더 큰 건물일경우
                if building[-1] > arr[right]:# 다음에 나오는 빌딩이 더 커야한다.( 막혀서 못감. )
                    break
            else: # 자기자신보다 더 작은 건물일경우 건물이 다른건물에 걸리는지 확인한다.
                if building[-1] < arr[right]:
                    for height in building:
                        for h in range(height-1, right - cur, -1):
                            if h < arr[right]:
        
        

                
        
        # 자신보다 낮은 건물일경우
        # 다음건물은 현재건물-1 이상 건물이어야한다.
        
        building.append(arr[right])
        right +=1
         
    
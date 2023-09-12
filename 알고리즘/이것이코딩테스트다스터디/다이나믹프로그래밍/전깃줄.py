# https://www.acmicpc.net/problem/2565
# 전깃줄을 하나씩 추가해 나아가면서 겹치는 TABLE을 업데이트한다.
# TABLE에서 가장 큰 값으로 SORTING 을 한뒤, 하나씩 빼가며 전기줄이 교차하는지 확인한다.
# 교차를 하지 않는다면 종료를하고 전체전깃줄의수 - 총 빼간값을 출력한다.

# 전기줄이 교차하는지 확인하는 로직 ( 핵심 로직 ).

# LIS 알고리즘으료 효과적으로 풀 수 있다. // 결론...

N = int(input())

queue = []
aqueue = []
dp = [0 for _ in range(501)]
for _ in range(N):
    a, b = map(int ,input().split())
    for x , y in queue:
        if (a > x and b < y) or (a < x and b > y): # 교차하는 조건
            dp[a] += 1
            dp[x] += 1
    
    queue.append((a,b))
    aqueue.append(a)

def isCrossed(queue):
    for i in range(len(queue)):
        for j in range(len(queue)):
            if i != j:
                a ,b = queue[i]
                x, y = queue[j]
                if (a > x and b < y) or (a < x and b > y):
                    return True
                
    return False

def removeMax(queue, aqueue):
    maxidx = dp.index(max(dp))
    dp[maxidx] = 0
    idx = aqueue.index(maxidx)
    queue.pop(idx)
    aqueue.pop(idx)          
    

while isCrossed(queue):
    removeMax(queue, aqueue)
    
print(N - len(queue))



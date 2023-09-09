# https://www.acmicpc.net/problem/2493
import sys
sys.setrecursionlimit(1000001)

N = int(input())
table = list(map(int, input().split()))

result = []
queue = []
queue.append([table[0], 1])
result.append(0) # 첫번째 인덱스는 레이저를 수신할 탑이 없다.


def findbybysect(start, end, queue, number):
 
    idx = (start + end) // 2
    
    if idx == 0:
        if queue[end][0] > number:
            return queue[end][1]
        else:
            if queue[start][0] > number:
                return queue[start][1]
            else:
                return -1
            
    if queue[end][0] > number:
        return queue[end][1]
    
    if queue[start][0] <= number:
        return -1
    
    if queue[idx][0] > number:
        findbybysect(idx-1, end, queue, number)
    else:
        findbybysect(start, idx, queue, number)
        
    

for i in range(1, len(table)):
    # queue에서 자기자신보다 큰 건물을 찾는다.  
    index = findbybysect(0, len(queue)-1,queue, table[i])
            
    if index == -1:
        result.append(0)
    else:
        result.append(index)
    
    # 큐에 마지막에 있는 값이 자기자신보다 작거나 같을 경우 자기자신으로 대체
    # 큐에 마지막에 있는 값이 자기자신보다 클경우는 큐 뒤에 추가한다.
    if table[i] >= queue[-1][0]:
        queue[-1][0] = table[i]
        queue[-1][1] = i+1
    else:
        queue.append([table[i], i+1])

print(*result)
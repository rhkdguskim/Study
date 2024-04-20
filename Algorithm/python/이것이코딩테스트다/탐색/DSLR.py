# https://www.acmicpc.net/problem/9019
# 너비 우선 탐색으로 문제를 해결한다.
# A값을 cost와 큐에 넣고 큐를 pop 하여 DSLR연산을 모두 수행한뒤 또 큐에 넣는다. ( 넣을때 연산의 누적을 cost에 넣는다.)
# 연산을 하고난뒤 B값과 같아지면 연산을 종료하고 누적 cost값을 출력한다.
# 너비우선탐색을 선택한 이유는 최소 연산개수 때문이다.

# 에러1) 메모리 초과 발생
# 숫자를 방문처리를 하여 이미 방문한 숫자는 방문하지 않게 조건을 추가한다.
# 에러2)시간 초과 발생
# L,R 를 구하는 연산을 좀더 스마트하게 바꾼다.

from collections import deque
T = int(input())
ops = ['D','S','L','R']

for _ in range(T):
    A, B = map(int, input().split())
    queue = deque()
    queue.append(A) # 값과 빈 배열을 넣는다.
    visited = [None for _ in range(10000)]
    visited[A] = ''
    while queue:
        register = queue.popleft()
        
        if register == B: # 만약 조건을 찾는다면
            print(visited[B])
            break
        
        for op in ops:
            if op == 'D': # D연산은 2배를 취한뒤, 9999보다 큰경우에는 10000으로 나눈 나머지 값으로 취한다.
                newregister = (register * 2) % 10000
            elif op == 'S': # -1을 한 결과를 레지스터리에 넣는다. 레지스터리가 0이라면 9999를 넣는다.
                newregister = (register - 1) % 10000
            elif op == 'L': # 왼편으로 회전시켜레지스터리에 저장한다.
                newregister = (register % 1000) * 10 + register // 1000
            elif op == 'R': # 오른편으로 레지스터를 저장한다.
                newregister = (register % 10) * 1000 + register // 10
            
            if visited[newregister] is None:
                visited[newregister] = visited[register] + op
                queue.append(newregister)
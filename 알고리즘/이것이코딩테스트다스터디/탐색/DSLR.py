# https://www.acmicpc.net/problem/9019
# 너비 우선 탐색으로 문제를 해결한다.
# A값을 cost와 큐에 넣고 큐를 pop 하여 DSLR연산을 모두 수행한뒤 또 큐에 넣는다. ( 넣을때 연산의 누적을 cost에 넣는다.)
# 연산을 하고난뒤 B값과 같아지면 연산을 종료하고 누적 cost값을 출력한다.
# 너비우선탐색을 선택한 이유는 최소 연산개수 때문이다.

# 에러1) 메모리 초과 발생
# 만약 A가 1111 일경우 무한으로 탐색할 수 있게된다. 따라서 변경된 값만 탐색가능하게 조건을 추가한다.
# 숫자를 방문처리를 하여 이미 방문한 숫자는 방문하지 않게 조건을 추가한다.
#
from collections import deque
T = int(input())
ops = ['D','S','L','R']
visited = [None for _ in range(10000)]
for _ in range(T):
    A, B = map(int, input().split())
    queue = deque()
    queue.append(A) # 값과 빈 배열을 넣는다.
    visited[A] = ''
    while queue:
        register = queue.popleft()
        newregister = 0
        if register == B: # 만약 조건을 찾는다면
            print(visited[register])
            break
        
        for op in ops:
            if op == 'D': # D연산은 2배를 취한뒤, 9999보다 큰경우에는 10000으로 나눈 나머지 값으로 취한다.
                newregister = register * 2
                if newregister > 9999:
                    newregister %= newregister
            elif op == 'S': # -1을 한 결과를 레지스터리에 넣는다. 레지스터리가 0이라면 9999를 넣는다.
                if register == 0:
                    newregister = 9999
                else:
                    newregister = register - 1
            elif op == 'L': # 왼편으로 회전시켜레지스터리에 저장한다.
                char = list(str(register)) # 문자열로 변환한다.
                temp = char[0] # 왼편 회전을 위하여 배열의 첫번째 인덱스를 temp값으로 둔다.
                for i in range(len(char)-1): # 배열을 0번부터 n-1까지 다음 인덱스의 값으로 초기화한다.
                    char[i] = char[i+1]
                char[-1] = temp # 마지막 배열의 값은 temp 값으로 초기화
                newchar = ''
                for c in char:
                    newchar += c
                newregister = int(newchar)
                    
            elif op == 'R': # 오른편으로 레지스터를 저장한다.
                char = list(str(register)) # 문자열로 변환한다.
                temp = char[-1] # 오른 회전을 위하여 배열의 마지막 인덱스를 temp값으로 둔다.
                for i in range(len(char)-2, 0, -1): # 배열을 n-1번부터 0까지 이전 인덱스의 값으로 초기화한다.
                    char[i] = char[i-1]
                char[0] = temp # 첫번째 배열의 값은 temp 값으로 초기화
                newchar = ''
                for c in char:
                    newchar += c
                newregister = int(newchar)
            
            if visited[newregister] == None:
                visited[newregister] = visited[register] + op
                queue.append(newregister)
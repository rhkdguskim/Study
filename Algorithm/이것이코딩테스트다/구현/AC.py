# https://www.acmicpc.net/problem/5430
from collections import deque
T = int(input()) # 테스트 케이스 개수

for _ in range(T):
    p = str(input())
    n = int(input())
    arr = str(input())
    
    # arr에 있는 내용을 파싱한다.
    arr = arr[1:len(arr)-1]
    arr = arr.split(',')
    newarr = deque()
    for i in range(len(arr)):   
        if arr[i] != '':
            newarr.append(int(arr[i]))
    
    iserror = False
    isreverse = False
    for i in range(len(p)):
        if p[i] == 'D': # D일경우
            if len(newarr) == 0:
                iserror = True
                break
            if isreverse: # 반대일경우 끝에 수를 pop
                newarr.pop()
            else :
                newarr.popleft() # 정방향일경우 맨앞에 있는 수를 pop
        else : # R일 경우
            isreverse = not isreverse
    
    if iserror:
        print("error")
    else:
        char = ''
        char += '['
        while newarr:
            num = 0
            if isreverse:
                num = newarr.pop()
            else:
                num = newarr.popleft()
            
            if len(newarr) == 0:
                char += str(num)
            else :
                char += str(num)+','
            
        char += ']'
        print(char)
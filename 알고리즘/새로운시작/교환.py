# https://www.acmicpc.net/problem/1039
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

number = list(str(N))


visited = [False for _ in range(N)]
cnt = 0
for i in range(len(number)):
    if int(number[i]) == 0:
        visited[i] = True
    else:
        cnt += 1 # 방문해야하는 개수
k = 0
def switch(idx, idx2):
    temp = number[idx]
    number[idx] = str(number[idx2])
    number[idx2] = str(temp)
    
if cnt < 2:
    print(-1)
else:
    while K > k:
        if cnt == 2:
            break
        
        # 가장 큰수를 찾는다.
        idx = 0
        num = 0
        for i in range(len(number)):
            if not visited[i] and int(number[i]) >= num:
                idx = i
                num = int(number[i])

        # 맨 앞자리중 방문처리가 되지 않는 자리수를 찾는다.
        idx2 = 0
        for i in range(len(number)):
            if not visited[i]:
                idx2 = i
                break
        
        # 둘의 자리를 바꾼다. 맨앞자리를 방문처리해준다.
        switch(idx, idx2)
        
        # 2이상인 경우만 방문처리 해준다.
        if cnt > 2:
            visited[idx2] = True
            cnt -= 1
        
        if idx != idx2: 
            k += 1
        
        
    if cnt == 2:
        etc = [i for i in range(len(number)) if visited[i] == False]
        if K- k % 2 == 1:
            switch(etc[0], etc[1])
            
    print(''.join(number))
# https://www.acmicpc.net/problem/1644
N = int(input())

def getPrimelist(N):
    temp = [True for _ in range(N+1)]
    temp[0] = False # 0 은 소수가 아니다.
    temp[1] = False
    m = int(N ** 0.5) # 소수이기 판별할때에는 제곱근 까지만 판별하면됨
    for i in range(2,m+1):
        if temp[i] == True: # 해당 원소가 소수이면 다른 배수들은 소수가아니다.
            for j in range(i+i, N+1, i):
                temp[j] = False
                
    return list(i for i in range(len(temp)) if temp[i] == True)

Primelist = getPrimelist(N)
if Primelist:
    p1 = 0
    p2 = 1
    value = Primelist[0]
    result = 0
    while True:
        if len(Primelist)-1 == p2 and value <= N or len(Primelist)-1 == p1 :
            if value == N:
                result += 1 
            break
        
        if N > value:
            value += Primelist[p2]
            p2 += 1
        else:
            if value == N:
                result += 1
            value -= Primelist[p1]
            p1 += 1
            
    if N in Primelist:
        if N == 2:
            print(result)
        else:
            print(result+1) # 자기자신이 소수이면 자기자신 하나 카운트
    else:
        print(result)
else:
    print(0)
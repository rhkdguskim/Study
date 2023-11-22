# https://www.acmicpc.net/problem/1806
INF = int(1e9)
N, S = map(int, input().split()) # N은 수열의개수, S는 부분집합의 합
arr = list(map(int, input().split()))


p1 = 0
p2 = 1
value = arr[0]
currentlen = 1
minlength = INF
while True:
    if (N == p2 and value < S) or (N == p1): # end가 도달했을경우
        if value >= S:
            minlength = min(minlength, currentlen)
        break
    
    if value < S: # 현재 value 값이 부분의 합보다 작다면
        value += arr[p2] # p2 를 더한다
        p2 += 1 # p2를 1증가한다
        currentlen += 1

    else:
        minlength = min(minlength, currentlen)
        value -= arr[p1] # p1 값을 뺀다
        p1 += 1 # p1 값을 더한다
        currentlen -= 1
        

        
if minlength == INF:
    print(0)
else:
    print(minlength)

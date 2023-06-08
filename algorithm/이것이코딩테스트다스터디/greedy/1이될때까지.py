# 어떠한 수 N이 1이 될 때까지 다음의 두 과정중 하나를 반복적으로 선택하여 수행하려고 한다. 단, 두 번째 연산은 n이 K로 나누어 질때만 선택할 수있다.
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다.
# 실행하는 최소 횟수값을 구하여라
# 나누는것이 제일 우선이다.
N , K = map(int, input().split())

print(N, K)

counter = 0
while ( N != 1) :
    # N이 K로 나누어질때만 나누기연산을 한다.
    if(N % K == 0) : # 나눈 나머지 값이 0이면 나눌수 있다는거
        N //= K # N을 K로 나눈다.
    else : # 그렇지 않으면 N에서 1을 뺀다.
        N -= 1
    
    counter += 1
        
print(counter)
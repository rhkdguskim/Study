# 거스름돈으로 사용할 돈이 500원, 100원, 50원, 10원짜리 일때
# 동전 개수를 최소의 값을 구하는 개수를 구하여라

n = int(input())
coin_type = [500, 100, 50, 10]
count = 0
for coin in coin_type :
    count += n // coin
    n %= coin
    
print(count)
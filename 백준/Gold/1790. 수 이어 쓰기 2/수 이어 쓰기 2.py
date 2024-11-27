import sys
input = sys.stdin.readline

N, K = map(int, input().split())

cnt = 0
n = 1

while True:
    num_count = 9 * (10 ** (n - 1))
    digit_count = num_count * n
    
    if K <= digit_count:
        break
    
    K -= digit_count
    n += 1
index_in_numbers = (K - 1) // n
digit_index = (K - 1) % n


start_number = 10 ** (n - 1)
target_number = start_number + index_in_numbers

if target_number > N:
    print(-1)
else:
    print(str(target_number)[digit_index])
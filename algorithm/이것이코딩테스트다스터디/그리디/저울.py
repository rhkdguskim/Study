# https://www.acmicpc.net/problem/2437

# 작은수부터 정렬 한다음
# 작은수부터 하나하나 더해가면서 결과를 확인해본다.

N = int(input())
arr = list(map(int,input().split()))
arr.sort()

number = 1

while arr:
    cur_number = arr.pop(0)
    
    if cur_number > number:
        break
    else:
        number += cur_number

print(number)
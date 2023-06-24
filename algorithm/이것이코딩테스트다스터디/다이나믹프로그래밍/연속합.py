# https://www.acmicpc.net/problem/1912
N = int(input())
array = list(map(int, input().split()))

result = 0
maxvalue = 0
for i in range(0, N):
    result += array[i]
    if result > maxvalue:
        maxvalue = result
    
    if result < 0:
        result = 0
        
if maxvalue == 0:
    print(max(array))
else:
    print(maxvalue)
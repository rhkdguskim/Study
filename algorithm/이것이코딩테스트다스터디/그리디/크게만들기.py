# https://www.acmicpc.net/problem/2812
N, K = map(int, input().split())
number = str(input())

maxnumber = 0
maxidx = 0
for i in range(K):
    num = int(number[i])
    if num > maxnumber:
        maxnumber = num
        maxidx = i

newnumber = number[maxidx:]
print(maxidx)
counter = N - maxidx+1
print(counter)
result = ''

for i in range(len(newnumber)):
    if len(newnumber)-1 > i and int(newnumber[i+1]) >= int(newnumber[i]) and counter > 0:
        counter -= 1
    else :
        result += newnumber[i]
        
print(result)
# https://www.acmicpc.net/problem/1339
# 1. 가장 큰 자리수를 가장 큰 숫자로 넣는다.
# 2. 자리수가 같은경우, 개수가 많은 숫자로 넣는다.

N = int(input())
charlist = []
num_char = {}

for _ in range(N):
    temp = list(input())
    charlist.append(temp)
    for t in range(len(temp)):
        num_char.setdefault(temp[t], 0)
        num_char[temp[t]] +=  pow(10, (len(temp) - t))
        
queue = []
numbers = [0,1,2,3,4,5,6,7,8,9]

for key in num_char:
    queue.append([num_char[key], key])
    
queue.sort(reverse=True)

new_dict = {}
for i in range(len(queue)):
    num = numbers.pop()
    new_dict.setdefault(queue[i][1], 0)
    new_dict[queue[i][1]] = num
    
ans = 0
for char in charlist:
    temp = ''
    for c in char:
        temp += str(new_dict[c])
    
    ans += int(temp)
    
print(ans)
    
    
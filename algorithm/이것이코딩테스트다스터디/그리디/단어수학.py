# https://www.acmicpc.net/problem/1339
N = int(input())
strarray = []
maxlen = 0
for _ in range(N):
    data = input()
    if len(data) > maxlen:
        maxlen = len(data)
    
    strarray.append(data)
    
strarray.sort(key=lambda i:len(i), reverse=True)
number = [0,1,2,3,4,5,6,7,8,9]
alpanumber = [[] for _ in range(maxlen+1)]

print(alpanumber)
for char in strarray:
    for j in range(len(char)):
        print(len(char) - j)
        alpanumber[len(char) - j].append(char[j])
        
print(alpanumber)


strdict = dict()
    
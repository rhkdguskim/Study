# https://www.acmicpc.net/problem/1339
N = int(input()) # 단어의 개수를 입력
maxlen = 10 # 알파벳의 개수가 최대 10개 이기때문에 maxlen을 10으로 설정한다.
queue = [[] for _ in range(maxlen)] # idx 9 : 10번째 자리를 가지고 있는 문자열 리스트, 8 : 9번째 자리를 가지고 있는 문자열 리스트

charlist = []
char = dict() # 각 알파벳마다 가치를 넣는다.
for _ in range(N):
    data = input()
    charlist.append(data)
    for i in range(len(data)):
        if data[i] not in char:
            char[data[i]] = 10**(len(data) - i)
        else :
            char[data[i]] += 10**(len(data) - i)

minqueue = [] # 우선순위 큐로 넣을 수 있지만 sort 한번만 해주는게 더 시간복잡도가 빠르기 때문에 일반리스트로 지정
for i in char:
    minqueue.append([char[i], i])

minqueue.sort()
newchar = dict()
idx = 0
numlist = [9,8,7,6,5,4,3,2,1,0]

while minqueue: # 큐를 하나씩 빼서 newchar에 최종 번호를 지정한다.
    number , char = minqueue.pop()
    newchar[char] = str(numlist[idx])
    idx += 1

result = 0
for char in charlist:
    for i in newchar:
        char = char.replace(i,newchar[i]) # 지정된 번호로 replace해준다.
        
    result += int(char) # replace한 결과를 결과에 추가한다.
    
print(result)
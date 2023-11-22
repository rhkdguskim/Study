from itertools import combinations
import heapq
m=['a','e','i','o','u']
p=[] #정답 list
l=int(input().split()[0])
n=input().split()
n_j=list(set(n)-set(m)) #자음 list

for i in combinations(n,l): #모음 1개이상 걸러내기
  for j in m:
    if j in i:
      p.append(''.join(sorted(list(i))))
      break

queue = []
for _ in range(len(p)): # 자음 2개이상 걸러내기
  a=0
  for b in range(len(n_j)):
    if n_j[b] in p[_]:
      a+=1
      if a>=2:
        heapq.heappush(queue, p[_])
        break
    
while queue:
    print(heapq.heappop(queue))
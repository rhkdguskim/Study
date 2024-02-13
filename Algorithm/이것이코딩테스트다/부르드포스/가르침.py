# https://www.acmicpc.net/problem/1062
from itertools import combinations

N, K = map(int, input().split())
northword = list(['a','n','t','i','c'])
alpabat = list(['b','d','e','f','g','h','j','k','l','m','o','p','q','r','s','u','v','w','x','y','z'])

words = list()

for _ in range(N):
    word = list(input())
    words.append(word)
    


learned = [False for _ in range(26)]

for alpa in northword:
    learned[ord(alpa)-ord('a')] = True


maxcounter = 0

if K-4 > 0:
    for alpalist in combinations(alpabat, K-5):
        count = 0
        
        for alpa in alpalist:
            learned[ord(alpa)-ord('a')] = True
            
        # 계산하는 로직과 max값 리뉴얼
        for word in words:
            canRead = True
            for temp in word:
                if not learned[ord(temp)-ord('a')]: # 배우지 않는 알파벳이 있다면
                    canRead = False
                    break
            
            if canRead:
                count += 1
                    
        if count > maxcounter:
            maxcounter = count
            
        for alpa in alpalist:
            learned[ord(alpa)-ord('a')] = False
            
    print(maxcounter)
else:
    print(0)

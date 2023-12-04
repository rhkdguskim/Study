# https://www.acmicpc.net/problem/1759
# 최소 한개의 모음과, 두개의 자음으로 구성되어있다. 증가하는 순서대로 배열됨.
# L이 도달했을때, 모음의개수와 자음음의 개수가 맞을때 카운팅한다.
import sys
input = sys.stdin.readline
mo_list = set(['a', 'e', 'i', 'o', 'u'])


L, C = map(int, input().split())
words = list(map(str, input().split()))
words.sort()

def dfs(word, ja, mo):
    if len(word) >= L:
        if ja >= 2 and mo >= 1:
            return [word]
        
        return []
    
    result = []
    for w in words:
        if w not in word:
            if len(word) and word[-1] > w:
                continue
            
            word += w
            if w in mo_list:
                result += dfs(word, ja, mo + 1)
            else:
                result += dfs(word, ja + 1, mo)
            
            word = word[:len(word)-1]
    return result
            
ans = dfs('', 0, 0)
for word in ans:
    print(word)
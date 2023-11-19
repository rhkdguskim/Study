#https://www.acmicpc.net/problem/2866
import sys
input = sys.stdin.readline

R, C = map(int, input().split()) # 행, 열

words =['' for _ in range(C)]

for _ in range(R):
    temp = input().strip()
    for j in range(C):
        words[j] += temp[j]
        
words.sort()

def search_cnt(array, query):
    start = 0
    end = len(array) - 1
    left_idx = None
    while start <= end:
        mid = (start + end) // 2
        temp = array[mid]
        if temp >= query:
            left_idx = mid
            end = mid - 1
        else:
            start = mid + 1
            
    start = 0
    end = len(array) - 1
    right_idx = None
    while start <= end:
        mid = (start + end) // 2
        temp = array[mid]
        if temp <= query:
            right_idx = mid
            start = mid + 1
        else:
            end = mid - 1
            
    #print(right_idx, left_idx, query, array)
    return right_idx - left_idx + 1
        
start = 1
ans = 0
while start < R:
    flag = False
    words = [word[1:] for word in words]
    words.sort()
    for word in words:
        s_cnt = search_cnt(words, word)
        #print(s_cnt, word, start)
        if s_cnt > 1: # 중복이 있다면
            flag = True
            break
        
    if flag:
        break
    else:
        ans += 1
        
    start += 1

print(ans)
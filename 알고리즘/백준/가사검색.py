# https://school.programmers.co.kr/learn/courses/30/lessons/60060
from bisect import bisect_left
from bisect import bisect_right

def solve(array, start, end):
    left = bisect_left(array, start)
    right = bisect_right(array, end)
    return right - left
    

def solution(words, queries):
    new_words = [[] for _ in range(100001)]
    reversed_new_words = [[] for _ in range(100001)]
    for word in words:
        new_words[len(word)].append(word)
        reversed_new_words[len(word)].append(word[::-1])
        
    # 단어순으로 정렬한다.
    for word in new_words:
        word.sort()
        
    for word in reversed_new_words:
        word.sort()
    
    answer = []
    for query in queries:
        if query[0] == '?':
            # 접미사가 ? 라면 거꾸로 뒤집어서 탐색한다.
            answer.append(solve(reversed_new_words[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z')))
        else:
            # 접두사가 ? 라면 그냥 탐색해본다.
            answer.append(solve(new_words[len(query)], query.replace('?', 'a'), query.replace('?', 'z')))
            
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))
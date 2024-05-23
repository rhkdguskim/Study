# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from collections import Counter
from itertools import combinations

def solution(orders, course):
    orders = [''.join(sorted(order)) for order in orders]
    
    answer = []
    
    for course_length in course:
        combinations_count = Counter()
        
        for order in orders:
            combinations_count.update(combinations(order, course_length))
        
        
        if combinations_count:
            max_count = max(combinations_count.values())
            answer.extend([''.join(combi) for combi in combinations_count if combinations_count[combi] == max_count and max_count > 1])
    
    return sorted(answer)
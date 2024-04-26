# https://school.programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    operation = [lambda x, y : x + y, lambda x, y : x - y]
    
    queue = []
    
    for op in operation:
        queue.append((op(0, numbers[0]), 0))
        
    answer = 0
    
    while queue:
        num, idx = queue.pop()
        
        if idx == len(numbers) - 1:
            if num == target:
                answer += 1    
            continue
        
        new_idx = idx + 1
        for op in operation:
            queue.append((op(num, numbers[new_idx]), new_idx))
            
    return answer

def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
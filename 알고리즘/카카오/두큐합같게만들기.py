# https://school.programmers.co.kr/learn/courses/30/lessons/118667
# 하나의 큐에 반으로 나눈수를 계속 확인한다.
# 숫자가 작다면 right queue에서 가져오고
# 숫자가 크다면 해당큐에서 뺀다. 빼고, 가져오는과정에서 sum 값을 유지하고, 값이 같아진다면 정답 출력, 다ㅓ하고 큐가 비어진다면 정답출력.
from collections import deque


def solution(queue1, queue2):
    left_sum = sum(queue1)
    right_sum = sum(queue2)
    
    total = left_sum + right_sum
    # 2로 나눈 나머지가 1인경우 두수의 합은 같을 수 없다.
    if total % 2 == 1:
        return -1
    
    total //= 2
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    cnt = 0
    
    while queue1:
        if left_sum == total:
            return cnt
        elif left_sum > total:
            num = queue1.popleft()
            left_sum -= num
        else:
            if not queue2:
                return -1
            num = queue2.popleft()
            queue1.append(num)
            left_sum += num

        cnt += 1
        
    return -1

queue1 = [3, 2, 7, 2] # 14
queue2 = [4, 6, 5, 1] # 16

print(solution(queue1, queue2))
# https://school.programmers.co.kr/learn/courses/30/lessons/150367

# 더미노드라면 문자열 뒤에 0을 추가
# 더미노드가 아니라면 문자열 뒤에 1을 추가
# 문자열에 저장된 이진수를 십진수로 변환한다.

# 이진트리에서 리프노드가 아닌 노드는 자신의 왼쪽 자식이 루트인 서브트리의 노드들보다 오른쪽에 있으며, 오른쪽 자식이 루트인 서브트리의 노드들보다 왼쪽에 있다고 가정한다.
# 해당 이진트리는 중위순회 이다.

# 해당수를 이진트리로 표현 할 수 있는지 없는지 판단하라

# 숫자를 이진수로 만든다.
# 길이가 짝수라면 양쪽끝에 0을 넣어본다 ( 가지수 2개)
# 첫번째 인덱스의 다음값은 무조건 1이다.
# 두번째 인덱스부터 탐색하면서 해당 인덱스의 값이 0이라면 i+1이 1 무조건이어야한다(자기자신의 루트노드이기때문)

# 가운데는 항상 루트노드이다.
# 루트 노드를 기준으로 왼쪽, 오른쪽을 분할정복한다.

def make_binary(number):
    if number == 0:
        return '0'
    
    temp = ''
    while number > 0:
        temp += str(number % 2)
        number = number // 2
        
    return temp[::-1]

def is_binary(binary):
    if len(binary) == 1:
        return True
    
    center = len(binary)//2
    if binary[center] == '1':
        return is_binary(binary[:center]) and is_binary(binary[center+1:])
    else:
        for l in range(center):
            if binary[l] == '1':
                return False
        
        for r in range(center+1, len(binary)):
            if binary[r] == '1':
                return False
            
        return True

        

def solution(numbers):
    answer = []
    for number in numbers:
        temp = make_binary(number)
        h = 0
        for i in range(1, int(1e9)):
            if pow(2,i) - 1 >= len(temp):
                h = pow(2,i) - 1
                break
        temp2 = '0'* (h - len(temp))
        
        if is_binary(temp2 + temp):
            answer.append(1)
        else:
            answer.append(0)
            
    return answer

numbers = [63, 111, 95]
print(solution(numbers))
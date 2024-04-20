import sys

input = sys.stdin.readline

def decode(char):
    if '0' <= char <= '9':
        return int(char)
    else:
        return ord(char) - ord('A') + 10

def encode(num):
    if num <= 9:
        return str(num)
    else:
        return chr(num - 10 + ord('A'))

def calculate_weight(numbers):
    weights = [0] * 36  # 각 숫자(0-9, A-Z)에 대한 가중치
    for number in numbers:
        for i, char in enumerate(reversed(number)):
            index = decode(char)
            weights[index] += 36**i
    return weights

def replace_with_z(numbers, to_replace):
    result = []
    for number in numbers:
        new_number = ''
        for char in number:
            if char in to_replace:
                new_number += 'Z'
            else:
                new_number += char
        result.append(new_number)
    return result

def sum_numbers(numbers):
    total = 0
    for number in numbers:
        current_sum = 0
        for char in number:
            current_sum = current_sum * 36 + decode(char)
        total += current_sum
    return total

def find_max_sum(numbers, k):
    weights = calculate_weight(numbers)
    to_replace = sorted(range(36), key=lambda i: weights[i], reverse=True)[:k]
    to_replace = {encode(i) for i in to_replace}
    replaced_numbers = replace_with_z(numbers, to_replace)
    total_sum = sum_numbers(replaced_numbers)
    return encode(total_sum)

# 입력 처리
N = int(input().strip())
numbers = [input().strip() for _ in range(N)]
K = int(input().strip())


max_sum = find_max_sum(numbers, K)
print(max_sum)

from functools import reduce

def solution(numbers):
    return str(int(reduce(lambda x, y: x + y, sorted(map(str, numbers), key=lambda x: x * 3, reverse=True))))
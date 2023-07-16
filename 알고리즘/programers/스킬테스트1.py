import math

def solution(n):
    result = math.sqrt(n)
    if(float(result) == int(result)) :
        return pow(result+1, 2)
    else:
        return -1

solution(16)
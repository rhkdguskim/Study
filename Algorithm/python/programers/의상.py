from collections import Counter
from functools import reduce
from operator import mul

def solution(clothes):
    return reduce(mul, map(lambda x:x+1, Counter([x[1] for x in clothes]).values())) - 1
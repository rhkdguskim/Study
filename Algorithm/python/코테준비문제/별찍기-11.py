#https://www.acmicpc.net/problem/2448
from copy import deepcopy
N = int(input())
star = []
star.append("*")
star.append("* *")
star.append("*****")

def makestar(star):
    if len(star) == N:
        return star
    
    newstar = deepcopy(star)
    for i in range(len(star)):
        empty = " " * len(star[len(star) -1 - i])
        newstar.append(star[i] + empty + star[i])
    
    return makestar(newstar)
        

result = makestar(star)

for i in range(len(result)):
    empty = " " * (len(result) - 1 - i)
    print(empty + result[i] + empty)
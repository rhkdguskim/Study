# https://www.acmicpc.net/problem/1461

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

NONE = -1
PLUS = 0
MINUS = 1

books = list(map(int, input().split()))
plus_books = []
minus_books = []

for book in books:
    if book > 0:
        plus_books.append(book)
    else:
        minus_books.append(abs(book))

plus_books.sort()
minus_books.sort()

def search():
    plus_value = 0
    minus_value = 0
    if plus_books:
        plus_value = abs(plus_books[-1])
    if minus_books:
        minus_value = abs(minus_books[-1])
        
    if plus_value == 0 and minus_value == 0:
        return NONE
    elif plus_value > minus_value:
        return PLUS
    else:
        return MINUS
    
def pop_value(arr : list):
    cnt = M
    max_value = 0
    while arr and cnt > 0:
        max_value = max(max_value, arr.pop())
        cnt -= 1
        
    return max_value

first_flag = True
ans = 0
while True:
    target = search()
    
    if target == NONE:
        break
    
    value = 0
    if target == PLUS:
        value = pop_value(plus_books)
    else:
        value = pop_value(minus_books)
    
    if first_flag == True:
        ans += value
        first_flag = False
    else:
        ans += value*2

print(ans)
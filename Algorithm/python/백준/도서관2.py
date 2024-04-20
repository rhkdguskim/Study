# https://www.acmicpc.net/problem/1461

N, M = map(int, input().split())
books = list(map(int, input().split()))

plus_books, minus_books = [], []
for book in books:
    if book < 0:
        minus_books.append(book)
    else:
        plus_books.append(book)

plus_books.sort(reverse=True)
minus_books.sort()

result = []
for i in range(0, len(plus_books), M):
    result.append(tuple(plus_books[i:i + M]))


for i in range(0, len(minus_books), M):
    result.append(tuple(minus_books[i:i + M]))

result.sort(key= lambda x: abs(x[0]))

ans = 0
for i in result[:len(result) - 1]:
    ans += abs(i[0]) * 2

ans += abs(result[-1][0])

print(ans)
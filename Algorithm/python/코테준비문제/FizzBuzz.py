import sys
input = sys.stdin.readline
N = int(input())
for i in range(1, N+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 and (i % 5):
        print("Fizz")
    elif i % 5 == 0 and (i % 3):
        print("Buzz")
    else:
        print(i)
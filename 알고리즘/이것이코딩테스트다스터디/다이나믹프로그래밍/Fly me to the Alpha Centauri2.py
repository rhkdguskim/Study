# https://www.acmicpc.net/problem/1011
from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    x, y = map(int, stdin.readline().split(" "))
    move = 1
    sum = 0
    while True:
        if y-x-1 > 1:
            sum += move
            if move == 1:
                if y - x == move:
                    break
            else:
                if sum-move < y-1-x <= sum:
                    break
                
            move += 1
        else:
            break

    if y-x == 1:
        print(1)
    elif y-x-1 == 1:
        print(2)
    else:
        print(move+1)
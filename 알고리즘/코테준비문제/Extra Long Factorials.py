# https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=true
import sys
input = sys.stdin.readline

def factoryial(n):
    if n == 1:
        return 1

    return n*factoryial(n-1)

print(factoryial(int(input())))
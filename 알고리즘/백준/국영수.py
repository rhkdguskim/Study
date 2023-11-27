# https://www.acmicpc.net/problem/10825
import sys
input = sys.stdin.readline
N = int(input())
student = []

for _ in range(N):
    temp = list(input().split())
    for i in range(1, len(temp)):
        temp[i] = int(temp[i])
    
    student.append(temp)
    
    
student.sort(key=lambda x : ((-x[1], x[2], -x[3], x[0])))

for s in student:
    print(s[0])
# https://www.acmicpc.net/problem/16120

# 1. 왼쪽부터 탐색해가며 PPAP를 찾는다.
# 2. PPAP 가 존재하면 P로 바꾼다.
# 1번과 2번을 반복한다. (문자열의 길이가 4보다 클때까지)
import sys
input = sys.stdin.readline

string = str(input().strip())

p_count = 0
a_count = 0

stack = []
for char in string:
    if stack and stack[-1] == 'A' and char == 'P' and p_count >= 2:
        p_count -= 2
        a_count -= 1
        
    if char == 'P':
        p_count += 1
    else:
        a_count += 1
        
    stack.append(char)
    
if p_count == 1 and a_count == 0:
    print("PPAP")
else:
    print("NP")
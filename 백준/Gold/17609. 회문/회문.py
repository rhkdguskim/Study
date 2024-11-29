import sys
input = sys.stdin.readline

# 투포인터
# left와 right가 같을경우는 left -=1, right -=1
# 다를경우
# 1. cnt가 0일때
# 2. left와 right-1이 같을경우는 right -=1
# 3. right와 left+1이 같을경우는 left +=1
# 4. 1, 2, 3 번을 다 만족 못할경우는 일반문자열

N = int(input())

def is_palindrome(w, left, right): 
    while left < right:
        if w[left] != w[right]:
            return False
        left += 1
        right -= 1
    return True

def solve(w):
    left, right = 0, len(w) - 1
    while left < right:
        if w[left] == w[right]:
            left += 1
            right -= 1
        else:
            remove_left = is_palindrome(w, left + 1, right)
            remove_right = is_palindrome(w, left, right - 1)
            if remove_left or remove_right:
                return 1
            else:
                return 2
    return 0

for _ in range(N):
    w = str(input().strip())
    print(solve(w))
# https://www.acmicpc.net/problem/5904

# 왼 + 중간값 + 우
import sys
input = sys.stdin.readline

N = int(input())
total_len = 3
mid = 0
while total_len < N:
    mid += 1
    total_len = total_len*2 + (3 + mid) # 중간값, 우를 더한다.
    

def moo(total_len, mid_len, N):
    if N <= 3:
        if N == 1:
            print("m")
        else:
            print('o')
        return
    
    left_len = (total_len - mid_len) // 2
    
    if N <= left_len: #왼쪽으로 재귀
        return moo(left_len, mid_len-1, N)
    
    if N > left_len + mid_len: # 오른쪽에 있는경우
        return moo(left_len, mid_len-1, N - (left_len + mid_len))
    
    
    if N - left_len == 1:
        print('m')
    else:
        print('o')
    


moo(total_len, mid + 3, N)
    

    
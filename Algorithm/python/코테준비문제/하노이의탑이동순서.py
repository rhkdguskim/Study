# https://www.acmicpc.net/problem/11729
# 재귀로 문제풀이

N = int(input())
queue = []
def hanoi(N, start, middle, end):
    if N == 1:
        queue.append([start,end])
        return
    
    hanoi(N-1, start, end, middle)
    queue.append([start,end])
    hanoi(N-1, middle, start, end)
    
hanoi(N,1,2,3)

print(len(queue))

for start, end in queue:
    print(start, end)
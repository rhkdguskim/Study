import sys

input = sys.stdin.readline

int(input())

ans = 0
for tmp in zip(sorted(list(map(int, input().split()))), 
               sorted(list(map(int, input().split())), reverse=True)):
    
    ans += tmp[0] * tmp[1]

print(ans)
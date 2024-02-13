N = int(input())
coin = list(map(int, input().split()))
coin.sort()

x = 0
for c in coin:
    if abs(x - c) > 1:
        break
    else:
        x += c
        
print(x+1)
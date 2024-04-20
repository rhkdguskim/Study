N = input()

ans = int(N[0])
i = 1
while i < len(N):
    if ans == 1 or ans == 0 or N[i] == 1 or N[i] == 0:
        ans += int(N[i])
    else:
        ans *= int(N[i])
        
    i += 1

print(ans)
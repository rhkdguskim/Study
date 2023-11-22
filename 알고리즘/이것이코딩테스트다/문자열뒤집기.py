N = input()

number = int(N[0])
zero = 0
one = 0
if number == 1:
    one += 1
else:
    zero += 1
    
for i in range(1, len(N)):
    if number != int(N[i]):
        if int(N[i]) == 0:
            zero += 1
        else:
            one += 1
        number = int(N[i])


print(min(one, zero))
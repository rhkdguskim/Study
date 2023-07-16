# https://www.acmicpc.net/problem/9935
char = input()
bumpchar = input()
while bumpchar in char:
    char = char.replace(bumpchar, "")
    
if char == "":
    print("FRULA")
else:
    print(char)

length = len(bumpchar)
stack = []
for i in range(len(char)):
    stack.append(char[i])
    if bumpchar == ''.join(stack[-length:]):
        for _ in range(length):
            stack.pop()

newstr = ''.join(stack)
if newstr == "":
    print("FRULA")
else:
    print(newstr)
move = {"L":[0,-1], "R":[0,1] , "U":[-1,0], "D":[1,0]}
n = int(input())
movearr = list(map(str, input().split()))

pos = [1,1]

for m in movearr :
    if(1 <= pos[1] + move[m][1] <= n and 1 <= pos[0] + move[m][0] <= n): # 공간을 이동할 수 있을때
       pos[1]  += move[m][1]
       pos[0]  += move[m][0]
       
print(pos[0], pos[1])
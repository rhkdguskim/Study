# https://www.acmicpc.net/problem/10828
N = int(input()) # 명령의 총 개수
cmd = ['push', 'pop', 'size', 'empty', 'top'] # 명령

cmdlist = []
for _ in range(N):
    cmdlist.append(input())

queue = []
for c in cmdlist:
    cmd = list(c.split())
    if(len(cmd) > 1): # 숫자와 함께 온 명령어라면
        queue.append(cmd[1])
    else : # 단일 명령어라면
        if(cmd[0] == 'pop'):
            if(len(queue) > 0): 
                print(queue.pop())
            else :
                print(-1)
        elif(cmd[0] == 'size'):
            print(len(queue))
        elif(cmd[0] == 'empty'):
            if(len(queue) == 0):
                print(1)
            else :
                print(0)
        elif(cmd[0] == 'top'):
            if(len(queue) > 0): 
                print(queue[len(queue)-1])
            else :
                print(-1)
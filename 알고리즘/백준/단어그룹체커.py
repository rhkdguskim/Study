# https://www.acmicpc.net/problem/1316
# 단어가 연속해서 나오면 되는데 한번 다른 문자가 나왔다가 다시 똑같은 문자가 나와서는 안된다.
# N은 100보다 작은 자연수이고, 단어수는 100이 기때문에 모든 단어를 순회하면서 문제 풀기 가능
# 현재 문자와 이전의 문자와 다르면 visit 처리를 하는데, 이미 visit 처리가 되어있다면 다른 문자가 나왔다가 다시 똑같은 문자가 나온 경우이다.
import sys
input = sys.stdin.readline

N = int(input())

def dfs(prev, depth):
    global ans
    if depth >= len(temp): # 최종 그룹단어인 개수 카운팅
        ans += 1
        return
    
    cur = temp[depth]
    if prev != cur:
        if visited[ord(cur) - ord('a')]: # 이미 방문한 문자라면(?)
            return
        else:
            visited[ord(cur) - ord('a')] = True # 방문처리 한다.
            dfs(cur, depth+1)
    else:
        dfs(cur, depth+1) # 같은 문자가 아니라면 계속 탐색해본다.
        
    
ans = 0
for _ in range(N):
    visited = [False for _ in range(26)] # 알파벳 개수가 26개이니 체크를 해보자
    temp = str(input().strip())
    visited[ord(temp[0]) - ord('a')] = True
    dfs(temp[0], 1)
    
print(ans)
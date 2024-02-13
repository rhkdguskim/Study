# https://www.acmicpc.net/problem/2263
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

rootindex = [0 for _ in range(n+1)]
for i in range(n):
    rootindex[inorder[i]] = i

def newgetPredorder(startin, endin, startpost, endpost):
    if startin > endin or startpost > endpost:
        return
    
    root = postorder[endpost]
    idx = rootindex[root]
    print(root, end= ' ') # 루트 노드 출력
    
    newgetPredorder(startin, idx-1, startpost, startpost - startin + idx-1) # 좌측 노드 출력
    newgetPredorder(idx+1, endin, endpost - endin + idx, endpost-1) # 우측 노드 출력
    
    
def getPreorder(inorder, postorder):
    # 배열의 길이가 1이 되면 종료
    if inorder and postorder:
        if len(inorder) == 1:
            print(inorder[0], end= ' ')
            return

        rootnode = postorder[-1]
        rootidx = inorder.index(rootnode)
        
        # 프리오더는 루트노드, 좌측노드, 우측노드를 출력한다.
        print(postorder[-1], end= ' ') # 루트노드출력
        getPreorder(inorder[:rootidx], postorder[:rootidx]) # 좌측노드 출력
        getPreorder(inorder[rootidx+1:], postorder[rootidx:len(postorder)-1]) # 우측노드 출력
    
#getPreorder(inorder, postorder)
newgetPredorder(0, n-1, 0, n-1)
    
    
    
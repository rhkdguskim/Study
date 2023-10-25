# https://www.acmicpc.net/problem/1991
import sys
input = sys.stdin.readline

graph = {}
N = int(input())

for _ in range(N):
    a, b, c = map(str, input().split()) # root, left, right
    graph[a] = [b, c]

def preorder(node):
    
    print(node, end='')
    
    left = graph[node][0]
    right = graph[node][1]

    if left != '.':
        preorder(left)
        
    if right != '.':
        preorder(right)
        
def inorder(node):
    
    left = graph[node][0]
    right = graph[node][1]

    if left != '.':
        inorder(left)
        
    print(node, end='')
        
    if right != '.':
        inorder(right)
    
def postorder(node):
    left = graph[node][0]
    right = graph[node][1]

    if left != '.':
        postorder(left)
        
    if right != '.':
        postorder(right)
        
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()

#https://www.acmicpc.net/problem/5639
import sys
sys.setrecursionlimit(10**6)

class Node(object):
    def __init__(self,data=None):
        self.data = data
        self.leftnode = None
        self.rightnode = None
    
        
    def insertNode(self, value):
        currentNode = self
        while True:
            if currentNode.data > value:
                if not currentNode.leftnode:
                    currentNode.leftnode = Node(value)
                    break
                else:
                    currentNode = currentNode.leftnode
            else:
                if not currentNode.rightnode:
                    currentNode.rightnode = Node(value)
                    break
                else:
                    currentNode = currentNode.rightnode
            

currentNode = Node(int(input()))

while True:
    try:
        currentNode.insertNode(int(input()))
    except:
        break
    

def postOrder(node):
    if node is None:
        return
    
    postOrder(node.leftnode)
    postOrder(node.rightnode)
    print(node.data)

def preOrder(node):
    if node is None:
        return
    
    print(node.data)
    preOrder(node.leftnode)
    preOrder(node.rightnode)
    
postOrder(currentNode)
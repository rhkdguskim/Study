# https://school.programmers.co.kr/learn/courses/30/lessons/17685
# 트라이 자료구조를 활용한다.

def solution(words):
    class Node():
        def __init__(self) -> None:
            self.child = {}
            self.data = None
            self.cnt = 0
            
    class Trie():
        def __init__(self) -> None:
            self.head = Node()
            
        def insert(self, string):
            current_node = self.head
            
            for char in string:
                
                if char not in current_node.child:
                    current_node.child[char] = Node()    
                
                current_node = current_node.child[char]
                current_node.cnt += 1
                
            current_node.data = string
            
        def search(self, string):
            cnt = 0
            current_node = self.head
            
            for char in string:
                cnt += 1
                
                if char in current_node.child:
                    current_node = current_node.child[char]
                
                if current_node.data == string or current_node.cnt == 1:
                    return cnt
                
            
    answer = 0
    trie = Trie()
    for w in words:
        trie.insert(w)
    
    for w in words:
        answer += trie.search(w)
        
    return answer
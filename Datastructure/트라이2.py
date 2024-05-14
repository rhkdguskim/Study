class Node():
    def __init__(self, key):
        self.children = {}
        self.key = key
        self.data = None
        
class Trie():
    def __init__(self):
        self.head = Node(None)
        
    def find_all(self):
        current = self.head
        
        words = []
        current_nodes = [current]
        
        while current_nodes:
            next_nodes = []
            for node in current_nodes:
                for child in node.children:
                    next_node = node.children[child]
                    word = next_node.data
                    next_nodes.append(next_node)
                    if word is not None:
                        words.append(word)
            
            current_nodes = next_nodes
        
        return words
    
    def insert(self, string):
        current = self.head
        
        for char in string:
            if char not in current.children:
                current.children[char] = Node(char)
            
            current = current.children[char]
        
        current.data = string
        
    def remove(self, string):
        current = self.head
        
        def dfs(node : Node, string):
            if len(string) == 0:
                if node.data is None:
                    return False
                else:
                    node.data = None
                    return len(node.children) == 0
                
            char = string[0]
            if char not in node.children:
                return False
            
            ret = dfs(node.children[char], string[1:])
            
            if ret == True:
                node.children.pop(char)
                return len(node.children) == 0
            else:
                return False
            
        dfs(current, string)
        
    
    def search(self, string):
        current = self.head
        
        for char in string:
            if not char in current.children:
                return False
            
            current = current.children[char]
            
        return current.data != None
    
    
    def startwith(self, prefix):
        current = self.head
        
        for p in prefix:
            if not p in current.children:
                return None
            
            current = current.children[p]
        
        words = []
        
        if current.data:
            words.append(current.data)
        
        current_nodes = [current]
        
        while current_nodes:
            next_nodes = []
            for node in current_nodes:
                for key in node.children.keys():
                    word = node.children[key].data
                    if word is not None:
                        words.append(word)
                    
                    next_nodes.append(node.children[key])
            
            current_nodes = next_nodes
        
        return words
    
trie = Trie()
trie.insert("aaa")
trie.insert("aaa1")
trie.insert("aaa2")
trie.insert("aaa3")
trie.insert("aaa4")
trie.insert("aaa5")
trie.remove("aaa5")

print(trie.find_all())
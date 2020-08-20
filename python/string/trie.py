class Node:
    def __init__(self):
        self.common = 0
        self.nex = [-1]*26
        self.accept = False
        
class Trie:
    def __init__(self):
        self.char_size = 26
        self.base = 'a'
        self.nodes = [Node()]
    
    def insert(self, word):
        node_id = 0
        
        for wi in word:
            c = ord(wi)-ord(self.base)
            next_id = self.nodes[node_id].nex[c]
            
            if next_id==-1:
                next_id = len(self.nodes)
                self.nodes.append(Node())
                self.nodes[node_id].nex[c] = next_id
            
            self.nodes[node_id].common += 1
            node_id = next_id
        
        self.nodes[node_id].common += 1
        self.nodes[node_id].accept = True
    
    def search(self, word, prefix=False):
        node_id = 0
        
        for wi in word:
            c = ord(wi)-ord(self.base)
            next_id = self.nodes[node_id].nex[c]

            if next_id==-1:
                return False
            
            node_id = next_id
        
        return prefix or self.nodes[node_id].accept
    
    def count(self):
        return self.nodes[0].common

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


"""
TimeComplexity is O(m)
SpaceComplexity is O(m)
"""
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertString(self, word):
        current = self.root
        for ch in word:
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.endOfString = True
        print("successfully inserted.")


newTrie = Trie()
newTrie.insertString("API")
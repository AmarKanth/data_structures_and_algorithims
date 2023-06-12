class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    """
    TimeComplexity is O(m)
    SpaceComplexity is O(m)
    """
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

    """
    TimeComplexity is O(m)
    SpaceComplexity is O(m)
    """
    def searchString(self, word):
        currentNode = self.root
        for ch in word:
            node = currentNode.children.get(ch)
            if node == None:
                return False
            currentNode = node
        return currentNode.endOfString


newTrie = Trie()
newTrie.insertString("API")
newTrie.searchString("AP")
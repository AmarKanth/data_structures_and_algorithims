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


"""
If some part of given word is part of the word(API, APPLE)
     A
    /
   P
  / \
 I   P
      \
       L
        \
         E

If given string prefix is part of other string(API, APIS)
     A
    /
   P
  / \
 I   P
  \   \
   S   L
        \
         E
"""
def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    # If the node has morethan one chidren
    # Loop it to next character
    if len(currentNode.children) >= 1:
        deleteString(currentNode, word, index+1)
        return False
    
    # When index at last character in the word
    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            # Delete Characters will be happen 
            # from leaf node to first node
            root.children.pop(ch)
            return True
    
    # If the given word is prefix of other
    # we cant delete the word
    if currentNode.endOfString == True:
        deleteString(currentNode, word, index+1)
        return False
    
    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False

newTrie = Trie()
newTrie.insertString("APPLE")
newTrie.insertString("API")

deleteString(newTrie.root, "API", 0)
print(newTrie.searchString("API"))
print(newTrie.searchString("APPLE"))
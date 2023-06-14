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
CASE-1 : Some part of given string(API) is part of other string.
     A
    /
   P
  / \
 I   P
  \   \
   *   L
        \
         E
          \
           *

CASE-2 : Enire given string(API) is part of other string.
     A
    /
   P
  / \
 I*   P
  \   \
   S   L
    \   \
     *   E
          \
           *

CASE-3 : Other string(API) is Sub-Part of given String(APIS)
     A
    /
   P
  / 
 I*  
  \  
   S
    \
     *

CASE-4 : Not any node depends on this string K
     AK
    /  \
   P    *
  / 
 I  
  \  
   S
    \
     *
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
newTrie.insertString("API")
newTrie.insertString("APIS")

deleteString(newTrie.root, "APIS", 0)
print(newTrie.searchString("APIS"))
print(newTrie.searchString("API"))
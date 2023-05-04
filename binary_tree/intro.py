"""
1. In tree data stracture parent node has two attributes to maintain
data and list of links to sub-category nodes.
2. trees are non-linear data stractures.
3. In binary tree each node has most two children.
"""

"""
Basic Tree
"""
class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children
    
    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode("Drinks", [])

cold = TreeNode("Cold", [])
hot = TreeNode("Hot", [])
tree.addChild(cold)
tree.addChild(hot)

tea = TreeNode("Tea", [])
coffee = TreeNode("Coffee", [])
cola = TreeNode("Cola", [])
fanta = TreeNode("Fanta", [])
cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)

print(tree)


"""
Types Of BinaryTree

1. Full Binary Tree     :-  Each node should have 2 children or zero children
2. Perfect Binary Tree  :-  All the non-leaf nodes has two children and are at the same level(depth), 
                            all leaf nodes has zero children and are the same level(depth)
3. Complete Binary Tree :-  All levels are completely filled except last level.
4. Balanced Binary Tree :-  All the leaf nodes are in same level(depth)
"""

"""
Types of Traversal Methods

preorder    :- All-LeftNodes --> All-RightNodes
inorder     :- LeftNode --> RootNode --> RightNode
postorder   :- LeftNode --> RightNode --> RootNode
levelorder  :- Depth-1 --> Depth-2 --- Till-LastNode
"""
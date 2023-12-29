class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children
    
    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    
    def addChild(self, tree_node):
        self.children.append(tree_node)


tree = TreeNode("Drinks", [])
cold = TreeNode("Cold", [])
hot = TreeNode("Hot", [])
tree.addChild(cold)
tree.addChild(hot)

tea = TreeNode("Tea", [])
coffee = TreeNode("Coffee", [])
hot.addChild(tea)
hot.addChild(coffee)

cola = TreeNode("Cola", [])
fanta = TreeNode("Fanta", [])
cold.addChild(cola)
cold.addChild(fanta)

print(tree)
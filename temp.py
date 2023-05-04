class BTree:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children
    
    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+2)
        return ret
    
    def appendChild(self, childNode):
        self.children.append(childNode)

rootnode = BTree("Drinks", [])

hot = BTree("Hot", [])
cold = BTree("Cold", [])
rootnode.appendChild(hot)
rootnode.appendChild(cold)

tea = BTree("Tea", [])
coffee = BTree("Coffee", [])
hot.appendChild(tea)
hot.appendChild(coffee)

cola = BTree("Cola", [])
cold.appendChild(cola)

print(rootnode)
class TreeNode:
    def __init__(self,data,children=[]):
        self.data = data
        self.children = children
    
    def __str__(self):
        return str(self.data)
    
    def addChild(self,data):
        node = TreeNode(data)
        self.children.append(node)


newTree = TreeNode(5)
newTree.addChild(10)
print(newTree)
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.childrens = []
        self.parent = None

    def addChild(self,child):
        child = TreeNode(child)
        child.parent = self
        self.childrens.append(child)

    def __str__(self):
        return self.data
    
p = TreeNode("President")
p.addChild("Vice President")
print(p.childrens)
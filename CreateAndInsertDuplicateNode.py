class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insertDuplicateNode(root):
    if root == None:
        return  
    dup = BinaryTreeNode(root.data)
    save = root.left
    root.left = dup
    dup.left = save 
    insertDuplicateNode(save)
    insertDuplicateNode(root.right)    

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrder(root):
    if root==None:
        return
    print(root.data,end=" ")    
    preOrder(root.left)    
    preOrder(root.right)

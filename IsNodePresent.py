class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isNodePresent(root, x):
    if root == None:
        return False
    if root.data==x:
        return True
    left = isNodePresent(root.left,x) 
    right = isNodePresent(root.right,x) 
    return left or right    
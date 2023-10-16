class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def height(root) :
    if root==None:
        return 0 
    left = height(root.left)
    right = height(root.right)
    return 1+max(left,right)    
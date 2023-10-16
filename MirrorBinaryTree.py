class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None




def mirrorBinaryTree(root) :
    if root==None:
        return None
    temp = root.left
    root.left = root.right
    root.right = temp 
    mirrorBinaryTree(root.left)
    mirrorBinaryTree(root.right) 
    return root  
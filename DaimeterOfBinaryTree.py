class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findHeight(root):
    if root==None:
        return 0 
    leftHeight=findHeight(root.left)
    rightHeight=findHeight(root.right)

    if(leftHeight>rightHeight):
        return leftHeight+1
    else:
        return rightHeight+1        



def diameterOfBinaryTree(root) :
    if root==None:
        return 0 
    return findHeight(root.left)+findHeight(root.right)+1

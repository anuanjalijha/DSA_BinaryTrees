class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def countNodesGreaterThanX(root, x) :
    count = 0
    if root==None:
        return 0 
    left = countNodesGreaterThanX(root.left,x)
    right = countNodesGreaterThanX(root.right,x)   
    if root.data>x:
        return 1+left+right
    else:
        return left+right    

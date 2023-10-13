class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None




def getSum(root):
    if root is None:
        return 0 
    leftCount = getSum(root.left)
    rightCount = getSum(root.right)
    return root.data+leftCount+rightCount    

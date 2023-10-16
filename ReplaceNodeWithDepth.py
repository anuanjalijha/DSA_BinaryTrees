class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None




def changeToDepthTree(root,d=0) :
    if root==None:
        return
    
    root.data = d
    changeToDepthTree(root.left,d+1)
    changeToDepthTree(root.right,d+1) 
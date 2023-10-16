class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def printNodesWithoutSibling(root) :
    if root == None:
        return
    if root.left==None and root.right==None:
        return
    if root.left==None:
        print(root.right.data,end=" ")
        printNodesWithoutSibling(root.right)
    elif root.right==None:
        print(root.left.data,end=" ")
        printNodesWithoutSibling(root.left)
    else:
        printNodesWithoutSibling(root.left)
        printNodesWithoutSibling(root.right)


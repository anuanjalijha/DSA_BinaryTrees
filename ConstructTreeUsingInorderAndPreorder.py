class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def buildTree(preOrder, inOrder) :
    if len(preOrder)==0:
        return None
    rootData = preOrder[0]
    root=BinaryTreeNode(rootData)
    rootIndexInInOrder=-1
    for i in range(0,len(inOrder)):
        if inOrder[i]==rootData:
            rootIndexInInorder=i
            break 
    if rootIndexInInorder==-1:
        return None
    leftInorder=inOrder[0:rootIndexInInorder]
    rightInorder=inOrder[rootIndexInInorder+1:]
        
    lenLeftSubtree=len(leftInorder)
        
    leftPreorder=preOrder[1:lenLeftSubtree+1]
    rightPreorder=preOrder[lenLeftSubtree+1:]
        
    leftChild=buildTree(leftPreorder,leftInorder)
    rightChild=buildTree(rightPreorder,rightInorder)
        
    root.left=leftChild
    root.right=rightChild
    return root

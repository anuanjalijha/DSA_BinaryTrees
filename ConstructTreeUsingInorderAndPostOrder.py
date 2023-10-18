class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def buildTree(postOrder, inOrder) :
    if len(postOrder)==0:
        return None
    rootData=postOrder[-1]
    root=BinaryTreeNode(rootData)
    rootIndexInInOrder=-1
    for i in range(0,len(inOrder)):
        if inOrder[i]==rootData:
            rootIndexInInOrder=i
            break
    if rootIndexInInOrder==-1:
        return None
        
    leftInorder=inOrder[0:rootIndexInInOrder]
    rightInorder=inOrder[rootIndexInInOrder+1:]
        
    lenLeftSubtree=len(leftInorder)
        
    leftPostorder=postOrder[:lenLeftSubtree]
    rightPostorder=postOrder[lenLeftSubtree:-1]
        
    leftChild=buildTree(leftPostorder,leftInorder)
    rightChild=buildTree(rightPostorder,rightInorder)
        
    root.left=leftChild
    root.right=rightChild
    return root

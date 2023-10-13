class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def postOrder(root):
    if root is None:
        return   
    
    postOrder(root.left)
          
    postOrder(root.right)
    print(root.data,end=" ")
           
        

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelWise(root):
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print(current_node.data,end=':')
        if current_node.left is not None:
            q.put(current_node.left)
            print('L:'+str(current_node.left.data),end=',')
        else:
            print("L:-1",end=',')
        if current_node.right!=None:
            q.put(current_node.right)
            print("R:"+str(current_node.right.data),end='')
        else:
            print("R:-1",end='')
        print()    
        
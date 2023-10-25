from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelWise(root):
    q = queue.Queue()
    q.put(root)
    q.put(None)
    while not q.empty():
        current_node = q.get()
        if current_node is None:
            print()
            if not q.empty():
                q.put(None)
        else:
            print(current_node.data,end=" ")
            if current_node.left is not None:
                q.put(current_node.left)
            if current_node.right!=None:
                q.put(current_node.right)
           
    
    #Your code goes here





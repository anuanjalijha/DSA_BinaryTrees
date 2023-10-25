from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def helperFunction(root,path,k):
    if root is None:
        return 
    k = k-root.data
    path.append(root.data)
    if root.left==None and root.right==None:
        if k==0:
            for ele in path:
                print(ele,end=" ")
            print()
        path.pop()
        return 
    helperFunction(root.left,path,k)
    helperFunction(root.right,path,k)
    path.pop()                        



def rootToLeafPathsSumToK(root, k):
    path = []
    helperFunction(root,path,k)
	#Your code goes here



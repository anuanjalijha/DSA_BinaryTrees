from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def findKNodesDown(root, k):
    if root is None:
        return
    
    if k == 0:
        print(root.data)
        return
    
    findKNodesDown(root.left, k - 1)
    findKNodesDown(root.right, k - 1)        


def nodesAtDistanceK(root, node, k) :
    if root is None:
        return -1

    if root.data == node:
        findKNodesDown(root, k)
        return 0

    leftDist = nodesAtDistanceK(root.left, node, k)
    if leftDist != -1:
        if leftDist + 1 == k:
            print(root.data)
        else:
            findKNodesDown(root.right, k - leftDist - 2)
        return 1 + leftDist

    rightDist = nodesAtDistanceK(root.right,node, k)
    if rightDist != -1:
        if rightDist + 1 == k:
            print(root.data)
        else:
            findKNodesDown(root.left, k - rightDist - 2)
        return 1 + rightDist
    return -1    


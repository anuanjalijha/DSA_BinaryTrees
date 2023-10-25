from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)
MAX_VALUE = 9999999999
MIN_VALUE =   -9999999999


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



#Representation of the Pair Class
class Pair :

    def __init__(self, minimum, maximum) :
        self.minimum = minimum
        self.maximum = maximum



def getMinAndMax(root) :
    if root is None:
        return Pair(MAX_VALUE,MIN_VALUE)

    leftChild = getMinAndMax(root.left)
    rightChild = getMinAndMax(root.right)

    # Calculate the smallest and largest values
    smallest = min(root.data, leftChild.minimum, rightChild.minimum)
    largest = max(root.data,leftChild.maximum,rightChild.maximum)

    return Pair(smallest,largest)


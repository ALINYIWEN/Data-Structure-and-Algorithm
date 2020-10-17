# Types of binary tree

# Creating a node
class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

# Calculate height
class CalculateHeight:
    def __init__(self):
        self.CalculateHeight = 0

# Calculate the depth
def calculateDepth(node):
    d = 0
    while (node is not None):
        d+=1
        node = node.leftChild
    return d  

# Count the number of nodes
def countNodes(root):
    if root is None:
        return 0
    return (1 + countNodes(root.leftChild) + countNodes(root.rightChild))   

# Checking full binary tree
def isFullTree(root):
    # Tree empty case
    if root is None:
        return True

    # Checking whether child is present
    if root.leftChild is None and root.rightChild is None:
        return True

    if root.leftChild is not None and root.rightChild is not None:
        return (isFullTree(root.leftChild) and isFullTree(root.rightChild))

    return False    
  

# Check if the tree is perfect binary tree
def isPerfectTree(root, d, level=0):
    # check if the tree is empty
    if (root is None):
        return True

    if (root.leftChild is None and root.rightChild is None):
        return (d == level+1)

    if (root.leftChild is None or root.rightChild is None):
        return False   

    return (isPerfectTree(root.leftChild, d, level + 1) and
            isPerfectTree(root.rightChild, d, level + 1))

# Check if the tree is complete binary tree
def isComplete(root, index, numberNodes):
    # Check if the tree is empty
    if root is None:
        return True

    if index >= numberNodes:
        return False

    return (isComplete(root.left, 2 * index + 1, numberNodes)
            and isComplete(root.right, 2 * index + 2, numberNodes))

# Check height balance
def isHeightBalance(root, CalculateHeight):
    left_height = CalculateHeight()
    right_height = CalculateHeight()

    if root is None:
        return True

    l = isHeightBalance(root.left, left_height)
    r = isHeightBalance(root.right, right_height)

    CalculateHeight.CalculateHeight = max(
        left_height.CalculateHeight, right_height.CalculateHeight) + 1

    if abs(left_height.CalculateHeight - right_height.CalculateHeight) <= 1:
        return l and r

    return False


##========================================================================##
## Full binary Tree

root = Node(1)

root.leftChild = Node(2)
root.rightChild = Node(3)

root.leftChild.leftChild = Node(4)
root.leftChild.rightChild = Node(5)

if isFullTree(root):
    print("The first tree is a full binary tree")
else:
    print("The first tree is not a full binary full")

##========================================================================##
## Perfect binary Tree

root = Node(1)
root.leftChild = Node(2)
root.rightChild = Node(3)
root.leftChild.leftChild = Node(4)
root.leftChild.rightChild = Node(5)
root.rightChild.leftChild = Node(4)
root.rightChild.rightChild = Node(5)

if (isPerfectTree(root, calculateDepth(root))):
    print("The second tree is a perfect binary tree")
else:
    print("The second tree is not a perfect binary tree")

##========================================================================##
## Complete Binary Tree

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

node_count = countNodes(root)
index = 0

if isComplete(root, index, node_count):
    print("The tree is a complete binary tree")
else:
    print("The tree is not a complete binary tree")

##========================================================================##
## Balanced Binary Tree

CalculateHeight = CalculateHeight()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

if isHeightBalance(root, CalculateHeight):
    print('The tree is balanced')
else:
    print('The tree is not balanced')

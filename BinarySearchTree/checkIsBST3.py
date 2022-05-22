class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def takeInput():
    rootData = int(input())
    if rootData == -1:
        return
    root = BinaryTreeNode(rootData)
    leftTree = takeInput()
    rightTree = takeInput()
    root.left = leftTree
    root.right = rightTree
    return root

def printTree(root):
    if root == None:
        return
    print(root.data,end=" : ")
    if root.left is not None:
        print(" L",root.left.data,end=", ")
    if root.right is not None:
        print(" R ",root.right.data,end=" ")
    print()
    printTree(root.left)
    printTree(root.right)

def checkIfBST(root,min_range,max_range):
    if root == None:
        return True
    if root.data < min_range or root.data > max_range:
        return False

    isLeftWithinConstraints = checkIfBST(root.left,min_range,root.data-1)
    isRightWithinConstraints = checkIfBST(root.right,root.data,max_range)

    return isLeftWithinConstraints and isRightWithinConstraints

root = takeInput()
printTree(root)
print(checkIfBST(root,-100000,100000))

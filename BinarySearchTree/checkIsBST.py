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


def minTree(root):
    if root == None:
        return 100000
    leftMin = minTree(root.left)
    rightMin = minTree(root.right)
    return min(leftMin,rightMin,root.data)

def maxTree(root):
    if root == None:
        return -100000
    leftMax = maxTree(root.left)
    rightMax = maxTree(root.right)
    return max(leftMax,rightMax,root.data)

def checkIfBST(root):
    if root == None:
        return True

    leftMax = maxTree(root.left)
    rightMin = minTree(root.right)

    if root.data > rightMin or root.data < leftMax:
        return False

    leftAns = checkIfBST(root.left)
    rightAns = checkIfBST(root.right)
    return leftAns and rightAns

root = takeInput()
printTree(root)
print(checkIfBST(root))


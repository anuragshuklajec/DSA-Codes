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

def checkIfBST(root):
    if root == None:
        return 100000,-100000,True

    leftMin,leftMax,isLeftBST = checkIfBST(root.left)
    rightMin,rightMax,isRightBST = checkIfBST(root.right)

    minimum = min(leftMin,rightMin,root.data)
    maximum = max(leftMax,rightMax,root.data)
    isTreeBST = True

    if root.data <= leftMax or root.data > rightMin:
        isTreeBST = False
    if not(isLeftBST) or not(isRightBST):
        isTreeBST = False

    return minimum,maximum,isTreeBST

root = takeInput()
printTree(root)
print(checkIfBST(root))


class binaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def takeInput():
    rootData = int(input())
    if rootData == -1:
        return
    root = binaryTreeNode(rootData)
    leftEle = takeInput()
    rightEle = takeInput()
    root.left = leftEle
    root.right = rightEle
    return root

def printBinaryTreePostOrder(root):
    if root == None:
        return
    printBinaryTreePostOrder(root.left)
    printBinaryTreePostOrder(root.right)
    print(root.data,end=" ")

root = takeInput()
printBinaryTreePostOrder(root)

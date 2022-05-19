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

def numberOfLeafNode(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    numLeafLeft = numberOfLeafNode(root.left)
    numLeafRight = numberOfLeafNode(root.right)
    return numLeafLeft + numLeafRight

root = takeInput()
print(numberOfLeafNode(root))

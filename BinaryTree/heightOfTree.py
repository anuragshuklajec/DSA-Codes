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

def heightOfTree(root):
    if root is None:
        return 0
    leftHeight = heightOfTree(root.left)
    rightHeight = heightOfTree(root.right)
    return 1 + max(leftHeight,rightHeight)
root = takeInput()
print(heightOfTree(root))

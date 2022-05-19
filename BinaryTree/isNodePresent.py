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

def isNodePresent(root,data):
    if root == None:
        return False
    if root.data == data:
        return True
    return isNodePresent(root.left,data) or isNodePresent(root.right,data)

root = takeInput()
data = int(input())
isNodePresent(root,data)

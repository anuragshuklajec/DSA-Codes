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

def nodesWithoutSibling(root):
    if root == None:
        return
    if root.left is not None and root.right is None:
        print(root.left.data,end=" ")

    if root.left is None and root.right is not None:
        print(root.right.data,end=" ")

    nodesWithoutSibling(root.left)
    nodesWithoutSibling(root.right)
    
root = takeInput()
data = int(input())
nodesWithoutSibling(root,data)

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

def printAtDepthK(root,k):
    if root == None:
        return -1
    if k == 0:
        print(root.data)
        return


    printAtDepthK(root.left,k-1)
    printAtDepthK(root.right,k-1)

root = takeInput()
printAtDepthK(root,2)

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

def largestNodeData(root):
    if root is None:
        return -1    # ideally return -inf
    leftLargest = largestNodeData(root.left)
    rightLargest = largestNodeData(root.right)
    return max(root.data,leftLargest,rightLargest)

root = takeInput()
print(largestNodeData(root))

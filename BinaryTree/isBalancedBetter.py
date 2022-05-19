class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def takeInput():
    newEle = int(input())
    if newEle == -1:
        return
    root = BinaryTreeNode(newEle)
    leftEle = takeInput()
    rightEle = takeInput()
    root.left = leftEle
    root.right = rightEle
    return root

def printBinaryTree(root):
    if root == None:
        return
    print(root.data,end=":")
    if root.left is not None:
        print("L",root.left.data,end=",")
    if root.right is not None:
        print("R",root.right.data,end="")
    print()
    printBinaryTree(root.left)
    printBinaryTree(root.right)

def isBalancedBetter(root):
    if root == None:
        return 0, True
    lh, isLeftBalanced = isBalancedBetter(root.left)
    rh, isRightBalanced = isBalancedBetter(root.right)
    h = 1 + max(lh,rh)
    if lh - rh > 1 or rh - lh > 1:
        return h, False
    return h, isLeftBalanced and isRightBalanced

root = takeInput()
printBinaryTree(root)
print(isBalancedBetter(root))



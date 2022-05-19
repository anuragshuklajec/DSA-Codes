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

def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left),height(root.right))

def isBalanced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if lh - rh > 1 or rh - lh > 1:
        return False
    isLeftBalanced = isBalanced(root.left)
    isRightBalanced = isBalanced(root.right)
    return isLeftBalanced and isRightBalanced

root = takeInput()
printBinaryTree(root)
print(isBalanced(root))



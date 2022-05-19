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

def removeLeaf(root):
    if root == None:
        return None

    if root.left == None and root.right == None:
        return None

    leftTree = removeLeaf(root.left)
    rightTree = removeLeaf(root.right)
    root.left = leftTree
    root.right = rightTree
    return root
root = takeInput()
printBinaryTree(root)
root = removeLeaf(root)
printBinaryTree(root)



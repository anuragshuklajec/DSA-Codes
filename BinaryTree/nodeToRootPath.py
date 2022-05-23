class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def takeInput():
    rootData = int(input())
    if rootData == -1:
        return
    root = BinaryTreeNode(rootData)
    leftTree = takeInput()
    rightTree = takeInput()
    root.left = leftTree
    root.right = rightTree
    return root

def printTree(root):
    if root == None:
        return
    print(root.data,end=" : ")
    if root.left is not None:
        print(" L",root.left.data,end=", ")
    if root.right is not None:
        print(" R ",root.right.data,end=" ")
    print()
    printTree(root.left)
    printTree(root.right)

def nodeToRootPath(root,s):
    if root == None:
        return None
    if root.data == s:
        l = list()
        l.append(root.data)
        return l

    leftOutput = nodeToRootPath(root.left,s)

    if leftOutput != None:
        leftOutput.append(root.data)
        return leftOutput
    rightOutput = nodeToRootPath(root.right,s)

    if rightOutput != None:
        rightOutput.append(root.data)
        return rightOutput

    else:
        return None

root = takeInput()
printTree(root)
print(nodeToRootPath(root,5))



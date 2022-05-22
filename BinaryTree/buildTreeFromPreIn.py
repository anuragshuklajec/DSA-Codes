import queue

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def takeInput():
    q = queue.Queue()
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    q.put(root)
    while not q.empty():
        current_node = q.get()
        leftChildData = int(input())
        if leftChildData != -1:
            leftChildNode = BinaryTreeNode(leftChildData)
            current_node.left = leftChildNode
            q.put(leftChildNode)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChildNode = BinaryTreeNode(rightChildData)
            current_node.right = rightChildNode
            q.put(rightChildNode)
    return root

def printTreeLevelWise(root):
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current_ele = q.get()
        print(current_ele.data,end=" ")
        if current_ele.left is not None:
            q.put(current_ele.left)
        if current_ele.right is not None:
            q.put(current_ele.right)

def buildTreeFromPreIn(pre,inorder):
    if len(pre) == 0:
        return None
    rootData = pre[0]
    root = BinaryTreeNode(rootData)
    rootIndexInInorder = -1
    for i in range(0,len(inorder)):
        if inorder[i] == rootData:
            rootIndexInInorder = i
            break
    if rootIndexInInorder == -1:
        return None

    leftInorder = inorder[0:rootIndexInInorder]
    rightInorder = inorder[rootIndexInInorder+1: ]

    lenLeftSubTree = len(leftInorder)

    leftPreorder = pre[1:lenLeftSubTree+1]
    rightPreorder = pre[lenLeftSubTree+1:]

    leftChild = buildTreeFromPreIn(leftPreorder,leftInorder)
    rightChild = buildTreeFromPreIn(rightPreorder,rightInorder)
    root.left = leftChild
    root.right = rightChild
    return root



pre = list(map(int,input().split()))
inorder = list(map(int,input().split()))
root = buildTreeFromPreIn(pre,inorder)
printTreeLevelWise(root)

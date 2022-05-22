import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def takeInputLevelWise():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print("Enter left child of ", current_node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)
        print("Enter right child of ", current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)
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


root = takeInputLevelWise()
printBinaryTree(root)

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def sortedArrayIntoBST(arr):
    if len(arr) == 0:
        return None
    mid = len(arr) // 2
    rootData = arr[mid]
    root = BinaryTreeNode(rootData)
    leftTree = sortedArrayIntoBST(arr[:mid])
    rightTree = sortedArrayIntoBST(arr[mid+1:])
    root.left = leftTree
    root.right = rightTree
    return root

import queue
def printTreeLevelWise(root):
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print(current_node.data,end=" ")
        if current_node.left is not None:
            q.put(current_node.left)
        if current_node.right is not None:
            q.put(current_node.right)

arr = list(map(int,input().split()))
root = sortedArrayIntoBST(arr)
printTreeLevelWise(root)

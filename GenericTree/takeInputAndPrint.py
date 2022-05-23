class GenericTreeNode:
    def __init__(self,data):
        self.data = data
        self.children = list()

def takeTreeInput():
    print("Enter root Data")
    rootData = int(input())
    
    if rootData == -1:
        return None

    root = GenericTreeNode(rootData)
    print("Enter number of children for ", rootData)
    
    childrenCount = int(input())
    for i in range(childrenCount):
        child = takeTreeInput()
        root.children.append(child)
    return root


def printTree(root):
    # Not a base case edge case
    if root == None:
        return
    print(root.data)
    for child in root.children:
        printTree(child)


def printTreeDetailed(root):
    if root == None:
        return
    print(root.data, " : ", end="")
    for child in root.children:
        print(child.data,",",end="")
    print()
    for child in root.children:
        printTreeDetailed(child)
root = takeTreeInput()
printTreeDetailed(root)

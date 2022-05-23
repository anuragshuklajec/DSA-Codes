class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.numNodes = 0

    def isPresentHelper(self,root,data):
        if root is None:
            return False
        if root.data == data:
            return True
        if root.data > data:
            return self.isPresentHelper(root.left,data)
        else:
            return self.isPresentHelper(root.right,data)

    def isPresent(self,data):
        return self.isPresentHelper(self.root,data)

    def insertHelper(self,root,data):
        if root == None:
            node = BinaryTreeNode(data)
            return node
        if root.data > data:
            root.left = self.insertHelper(root.left,data)
            return root
        else:
            root.right = self.insertHelper(root.right,data)
            return root

    def insert(self,data):
        self.numNodes+=1
        self.root = self.insertHelper(self.root,data)

    def min(self,root):
        if root == None:
            return 100000

        if root.left == None:
            return root.data

        return self.min(root.left)

    def deleteDataHelper(self,root,data):
        if root == None:
            return False, None
        if root.data > data:
            deleted,newLeft = self.deleteDataHelper(root.left,data)
            root.left = newLeft
            return deleted, root
        if root.data < data:
            deleted, newRight = self.deleteDataHelper(root.right,data)
            root.right = newRight
            return deleted, root

        # Root is Leaf
        if root.left == None and root.right == None:
            return True, root.right

        # Root has one child
        if root.left == None:
            return True, root.right

        if root.right == None:
            return True, root.left

        # Root has two children
        replacement = self.min(root.right)
        root.data = replacement
        deleted,newRightNode = self.deleteDataHelper(root.right,replacement)
        root.right = newRightNode
        return True, root



    def deleteData(self,data):
        deleted,newRoot = self.deleteDataHelper(self.root,data)
        if deleted:
            self.numNodes-=1
        self.root = newRoot
        return deleted

    def count(self):
        return self.numNodes

    def printTreeHelper(self,root):
        if root == None:
            return
        print(root.data,end=" : ")
        if root.left != None:
            print("L ",root.left.data,end=" , ")
        if root.right != None:
            print("R ",root.right.data,end=" ")
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)


    def printTree(self):
        self.printTreeHelper(self.root)


b = BST()
b.insert(10)
b.insert(5)
b.insert(12)
print(b.isPresent(10))
print(b.isPresent(7))
print(b.deleteData(4))
print(b.deleteData(10))
print(b.count())
b.printTree()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def takeInput():
    inputList = list(map(int,input().split()))
    head = None
    for curr in inputList:
        if curr == -1:
            break
        newNode = Node(curr)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

def printLL(head):
    while head:
        print(head.data,end=" -> ")
        head = head.next
    print("None")

def findAnodeRecursive(head,data,count):
    if head is None:
        return -1
    if head.data == data:
        return count
    return findAnodeRecursive(head.next,data,count+1)

head = takeInput()
printLL(head)
print(findAnodeRecursive(head,4,0))


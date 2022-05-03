class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = head
        else:
            tail.next = newNode
            tail = newNode
    return head

def printLL(head):

    while head is not None:
        print(head.data,end=" -> ")
        head =head.next
    print("None")
    return

head = takeInput()
printLL(head)

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
        if head == None:
            head = newNode
            tail = head
        else:
            tail.next = newNode
            tail = newNode
    return head
def printReversed(head):
    if head == None:

        return
    printReversed(head.next)
    print(head.data,end=" ")


head = takeInput()
printReversed(head)

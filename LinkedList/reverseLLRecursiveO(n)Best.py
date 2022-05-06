class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def takeInput():
    listInput = list(map(int,input().split()))
    head = None
    for curr in listInput:
        newNode = Node(curr)
        if curr == -1:
            break
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

def reverseLL(head):
    if head.next == None:
        return head

    smallHead = reverseLL(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallHead


head = takeInput()
printLL(head)
head = reverseLL(head)
printLL(head)

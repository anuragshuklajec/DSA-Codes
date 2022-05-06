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

def reverseLL(head):
    prev,curr = None,head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def printLL(head):
    while head:
        print(head.data,end=" -> ")
        head = head.next
    print("None")

head = takeInput()
printLL(head)
head = reverseLL(head)
printLL(head)

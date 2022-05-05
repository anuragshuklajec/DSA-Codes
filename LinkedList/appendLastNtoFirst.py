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

def lengthLL(head):
    if head  == None:
        return 0
    return 1 + lengthLL(head.next)


def printLL(head):
    while head:
        print(head.data,end=" -> ")
        head = head.next
    print("None")

def appendNtoLast(head,n):

    newN = lengthLL(head) - n

    curr = head
    prev = None

    while newN > 0:
        prev = curr
        curr = curr.next
        newN -= 1

    prev.next = None
    tempHead = head
    head = curr

    while curr.next is not None:
        curr = curr.next
    curr.next = tempHead
    return head

head = takeInput()
printLL(head)
printLL((appendNtoLast(head,3)))


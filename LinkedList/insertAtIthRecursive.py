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

def insertAtIth(head,i,data):
    if head is None:
        return None

    if i == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode

    smallHead = insertAtIth(head.next,i-1,data)
    head.next = smallHead
    return head

head = takeInput()
printLL(head)
head = insertAtIth(head,2,3)
printLL(head)

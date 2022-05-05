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

def deleteAtIth(head,i):
    if i < 0 :
        return head
    if head is None:
        return None

    if i == 0:
        return head.next

    smallHead = deleteAtIth(head.next,i-1)
    head.next = smallHead
    return head

head = takeInput()
printLL(head)
head = insertAtIth(head,2)
printLL(head)

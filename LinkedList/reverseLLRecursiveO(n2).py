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

def reverseLLRecursive(head):
    if head.next is None or head is None:
        return head
    smallHead = reverseLLRecursive(head.next)
    curr = smallHead
    while curr.next:
        curr = curr.next
    curr.next = head
    head.next = None
    return smallHead

def printLL(head):
    while head:
        print(head.data,end=" -> ")
        head = head.next
    print("None")

head = takeInput()
printLL(head)
printLL(reverseLLRecursive(head))

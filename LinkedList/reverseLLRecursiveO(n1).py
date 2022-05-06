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
        return head,head
    smallHead,tail = reverseLLRecursive(head.next)
    tail.next = head
    head.next = None
    return smallHead, head

def printLL(head):
    while head:
        print(head.data,end=" -> ")
        head = head.next
    print("None")

head = takeInput()
printLL(head)
smallHead,head = reverseLLRecursive(head)
printLL(smallHead)

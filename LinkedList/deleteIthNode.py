class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def takeInput():
    inputList = list(map(int,input().split()))
    head = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

def printLL(head):
    while head is not None:
        print(head.data,end=" -> ")
        head = head.next
    print("None")

def deleteIth(head,i):
    count = 0
    curr = head
    if i == 0:
        return curr.next
    while head and count < i:
        prev = curr
        curr = curr.next
        count+=1
    if curr.next is not None:
        prev.next = curr.next
    else:
        prev.next = None
    return head

head = takeInput()
printLL(head)
i = int(input())

printLL(deleteIth(head,i))





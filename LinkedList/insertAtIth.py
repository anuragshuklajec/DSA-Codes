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

def insertAtIth(head,ele,i):
    count = 0
    curr = head
    newNode = Node(ele)
    if i == 0:
        newNode.next = curr
        return newNode

    while curr is not None and count < i:
        prev = curr
        curr = curr.next
        count+=1
    prev.next = newNode
    newNode.next = curr
    return head

head = takeInput()
printLL(head)
i = int(input())
ele = int(input())
printLL(insertAtIth(head,ele,i))

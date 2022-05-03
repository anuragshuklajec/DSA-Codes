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


def printIthNode(head,i):
    count = 0
    while head is not None and count < i:
        head = head.next
        count+=1
    if head is None:
        return -1
    else:
        return head.data

head = takeInput()
printLL(head)
i = int(input())
print(printIthNode(head,i))


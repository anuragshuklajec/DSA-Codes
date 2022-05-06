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

def middleEle(head):
    slow = head
    fast = head
    while  fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

def printLL(head):
    while head:
        print(head.data,end=" -> ")
        head = head.next
    print("None")

head = takeInput()
printLL(head)
print(middleEle(head))

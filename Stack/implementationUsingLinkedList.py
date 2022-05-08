class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.__head = None
        self.__count = 0


    def push(self,item):
        newNode = Node(item)
        newNode.next = self.__head
        self.__head = newNode
        self.__count+=1

    def pop(self):
        if self.isEmpty():
            return None

        data = self.__head.data
        self.__head = self.__head.next
        self.__count-=1
        return data



    def top(self):
        if self.isEmpty():
            return None
        return self.__head.data


    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.top())
print(s1.pop())

print(s1.pop())

print(s1.pop())

print(s1.size())

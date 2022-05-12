class Node:
    def __init__(self,data):
        self.data = data
        self.next =None



class Queue:
    def __init__(self):

        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueu(self,ele):
        self.__newNode = Node(ele)
        if self.__head == None:
            self.__head = self.__newNode
        else:
            self.__tail.next = self.__newNode

        self.__tail = self.__newNode
        self.__count+=1



    def dequeue(self):
        if self.isEmpty():
            return -1
        ele = self.__head.data
        self.__count -=1
        self.__head = self.__head.next
        return ele

    def front(self):
        if self.isEmpty():
            return -1
        return self.__head.data

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

q = Queue()
q.enqueu(10)
q.enqueu(20)
q.enqueu(30)
print(q.dequeue())
print(q.front())
print(q.size())
print(q.isEmpty())

class Queue:
    def __init__(self):
        self.__arr = []
        self.__front = 0
        self.__count = 0

    def enqueu(self,ele):
        self.__arr.append(ele)
        self.__count+=1

    def dequeue(self):
        if self.isEmpty():
            return -1
        ele = self.__arr[self.__front]
        self.__count -=1
        self.__front +=1
        return ele

    def front(self):
        if self.isEmpty():
            return -1
        return self.__arr[self.__front]

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

class Stack:
    def __init__(self):
        self.__arr = []
        self.__count = 0

    def push(self,item):
        self.__arr.append(item)
        self.__count+=1

    def pop(self):
        if self.isEmpty():
            print("Empty Stack !")
            return
        self.__count -= 1
        return self.__arr.pop()

    def top(self):
        if self.isEmpty():
            print("Empty Stack !")
        return self.__arr[self.size()-1]


    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0


s1 = Stack()
s1.push(10)
s1.push(30)
s1.push(60)
print(s1.top())
print(s1.pop())
print(s1.size())
print(s1.pop())
print(s1.pop())


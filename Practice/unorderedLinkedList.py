
class Node:

    def __init__(self, initdata):
        self.next = None
        self.data = initdata

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        tmp = Node(item)
        tmp.setNext(self.head)
        self.head = tmp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while current != None:
            if current.getData == item
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        if self.head == None:
            self.head = Node(item)
            return

        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        tmp = Node(item)
        current.setNext(tmp)

    def insert(self,pos,item):
        current = self.head
        previous = None
        count = 1
        while count != pos:
            previous = current
            current = current.getNext()
            count += 1
        tmp = Node(item)
        tmp.setNext(current.getNext())
        current.setNext(tmp)

    def index(self,item):
        current = self.head
        count = 1
        while current != None:
            if current.getData() == item:
                return count
            else:
                current = current.getNext()

    # Removes the last item from the list
    def pop(self):
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        value = current.getData()
        previous.setNext(self.head)

    def printList(self):
        tmp = self.head
        while tmp:
            print(tmp.getData())
            tmp = tmp.getNext()




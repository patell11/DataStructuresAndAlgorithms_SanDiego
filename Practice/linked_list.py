
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setNext(self,newnext):
        self.next = newnext

    def getNext(self):
        return self.next

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
        curr = self.head
        count = 0
        while curr != None:
            count += 1
            curr = curr.getNext()
        return count

    def printList(self):
        if self.head == None:
            return
        else:
            curr = self.head
            while curr != None:
                print(curr.data, curr.next)
                curr = curr.getNext()

    def search(self,item):
        curr = self.head
        found = False
        while curr != None and not found:
            if curr.data == item:
                found = True
            else:
                curr = curr.getNext()
        return found

    def remove(self,item):
        curr = self.head
        prev = None
        found = False

        while not found:
            if curr.data == item:
                found = True
            else:
                prev = curr
                curr = curr.next

        if prev == None:
            self.head = curr.next
            curr.next = None
        else:
            prev.next = curr.next



# temp1 = Node(9)
# temp2 = Node(5)
# temp2.next = temp1
# print(temp1.data,temp1.next)
# print(temp2.data, temp2.next, temp2.next.data)

myList = UnorderedList()
myList.add(1)
myList.add(2)
myList.add(3)
myList.add(4)
myList.printList()
print(myList.search(3))
print("After deletion")
print(myList.remove(3))
myList.printList()
print("\n")
myList.remove((4))
myList.printList()
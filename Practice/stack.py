class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def peek2(self):
        if self.items == []:
            return "na"
        else:
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def getList(self):
        return self.items

# s=Stack()
#
# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())

def parChecker(symbolString):

    s = Stack()
    #print(s.pop())
    balanced = True
    pos = 0
    while pos < len(symbolString) and balanced:
        if symbolString[pos] in "([{":
            s.push(symbolString[pos])
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbolString[pos]):
                    #print(top, symbolString[pos])
                    balanced = False
        pos += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


print(parChecker('{({([][])}())}'))
print(parChecker('[{()]'))





class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, value):
        if self.leftChild == None:
            self.leftChild = BinaryTree(value)
        else:
            tmp = BinaryTree(value)
            tmp.leftChild = self.leftChild
            self.leftChild = tmp

    def insertRight(self,value):
        if self.rightChild == None:
            self.rightChild = BinaryTree(value)
        else:
            tmp = BinaryTree(value)
            tmp.rightChild = self.rightChild
            self.rightChild = tmp

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def getKey(self):
        return self.key

    def setRootVal(self, value):
        self.key = value

r = BinaryTree(None)
#print(r.getKey())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getKey())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getKey())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getKey())
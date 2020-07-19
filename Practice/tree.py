
class BinaryTree:
    def __init__(self, val):
        self.key = val
        self.leftchild = None
        self.rightchild = None

    def insertLeft(self, val):
        if self.leftchild == None:
            self.leftchild = BinaryTree(val)
        else:
            t = BinaryTree(val)
            t.leftchild = self.leftchild
            self.leftchild = t

    def insertRight(self, val):
        if self.rightchild == None:
            self.rightchild = BinaryTree(val)
        else:
            t = BinaryTree(val)
            t.rightchild = self.rightchild
            self.rightchild = t

    def getRightChild(self):
        return self.rightchild

    def getLeftChild(self):
        return self.leftchild

    def setRootVal(self, val):
        self.key = val

    def getRootVal(self):
        return self.key


r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())

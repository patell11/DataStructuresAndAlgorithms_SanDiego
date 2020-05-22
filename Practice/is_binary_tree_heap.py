
class isBinaryTreeHeap:
    def __init__(self, value):
        self.key = value
        self.leftchild = None
        self.rightchild = None

    def countNode(self, root):
        if root is None:
            return 0
        return (1 + self.countNode(root.leftchild) + self.countNode(root.rightchild))

    def isCompleteUtl(self, root, index, nodes_count):
        if root is None:
            return True
        if index >= nodes_count:
            return False
        return (self.isCompleteUtl(root.leftchild, 2*index+1, nodes_count) and
                self.isCompleteUtl(root.rightchild, 2*index+2, nodes_count))


    def isHeapUtl(self, root):
        if root.leftchild is None and root.rightchild is None:
            return True
        if root.rightchild is None:
            return root.key >= root.leftchild.key
        if root.rightchild and root.leftchild:
            return (root.key >= root.leftchild.key and
                    root.key >= root.rightchild.key and
                    self.isHeapUtl(root.leftchild) and
                    self.isHeapUtl(root.rightchild)
                    )
        return False

    def checkHeap(self):
        nodes_count = self.countNode(self)
        if (self.isCompleteUtl(self,0,nodes_count) and self.isHeapUtl(self)):
            return True
        else:
            return False

root = isBinaryTreeHeap(5)
root.leftchild = isBinaryTreeHeap(2)
root.rightchild = isBinaryTreeHeap(3)
root.leftchild.leftchild = isBinaryTreeHeap(1)


print(root.isCompleteUtl(root,0,4))
print(root.isHeapUtl(root))
print(root.checkHeap())
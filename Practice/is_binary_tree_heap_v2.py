

class isBinaryTreeHeap:
    def __init__(self, value):
        self.key = value
        self.leftchild = None
        self.rightchild = None

    def countNodes(self, root):
        if root is None:
            return 0
        return 1+ self.countNodes(root.leftchild) + self.countNodes(root.rightchild)

    def isCompleteUtl(self, root, index, num_nodes):
        if root is None:
            return True
        if index >= num_nodes:
            return False
        return self.isCompleteUtl(root.leftchild, 2*index+1, num_nodes) and \
                self.isCompleteUtl(root.rightchild, 2*index+2, num_nodes)

    def isHeapUtl(self,root):
        if root.leftchild is None and root.rightchild is None:
            return True
        if root.rightchild is None:
            return root.key >= root.leftchild.key
        if root.leftchild and root.rightchild:
            return root.key >= root.leftchild.key and root.key >= root.rightchild.key and \
                self.isHeapUtl(root.leftchild) and self.isHeapUtl(root.rightchild)
        return False

    def checkHeap(self, root):
        num_nodes = self.countNodes(root)
        return self.isCompleteUtl(root, 0, num_nodes) and self.isHeapUtl(root)

root = isBinaryTreeHeap(5)
root.leftchild = isBinaryTreeHeap(2)
root.rightchild = isBinaryTreeHeap(3)
root.leftchild.leftchild = isBinaryTreeHeap(1)


print(root.isCompleteUtl(root,0,4))
print(root.isHeapUtl(root))
print(root.checkHeap(root))


class TreeNode:
    def __init__(self, key, val ,left = None, right= None, parent = None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def getKey(self):
        return self.key

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        return succ

    def findMin(self):
        current = self
        while current.leftChild:
            current = current.leftChild
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        else:  ## if the node to be deleted has right child is the only possible case
            ## pointing to the child of the deleted node to the parent of the deleted node
            if self.isLeftChild():
                self.parent.leftChild = self.rightChild
            else:
                self.parent.rightChild = self.rightChild
            self.rightChild.parent = self.parent     # pointing the child to the parent of the deleted node

    # def inorderTraversal(self):
    #     if self:

    #def replaceNodeData(self, key, lc, rc):

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size


    ## add element to the binary search tree
    def put(self, key, val):
        if self.root:
            self._put(key, val,self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.hasLeftChild():
                self._put(key, val, current_node.leftChild)
            else:
                current_node.leftChild = TreeNode(key, val, parent = current_node)
        else:
            if current_node.hasRightChild():
                self._put(key, val, current_node.rightChild)
            else:
                current_node.rightChild = TreeNode(key, val, parent=current_node)

    def __setitem__(self, key, value):
        self.put(key, value)

    ## search a given element
    def get(self,key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    ## returns the node with the search key
    def _get(self, key, current_node):
        if not current_node:
            return None
        if current_node.key == key:
            return current_node
        if key < current_node.key:
            return self._get(key, current_node.leftChild)
        else:
            return self._get(key, current_node.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, item):
        if self.get(item):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            node_to_delete = self._get(key, self.root)
            if node_to_delete:
                self.remove(node_to_delete)
                self.size -= 1
            else:
                raise KeyError("Error, key not found")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, key not found")

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, current_node):
        if current_node.isLeaf():  ## if the node to be deleted is the leaf node
            if current_node.isLeftChild():
                current_node.parent.leftChild = None
            else:
                current_node.parent.rightChild = None
        elif current_node.hasBothChildren():  ## has both children
            succ = current_node.findSuccessor()
            succ.spliceOut()
            current_node.key = succ.key
            current_node.payload = succ.payload
        else:
            if current_node.hasLeftChild():
                if current_node.isLeftChild():
                    current_node.parent.leftChild = current_node.leftChild
                    current_node.leftChild.parent = current_node.parent
                elif current_node.isRightChild():
                    current_node.parent.rightChild = current_node.leftChild
                    current_node.leftChild.parent = current_node.parent
                else:
                    current_node.root = current_node.leftChild
                    current_node.leftChild.parent = None
            else:
                if current_node.isLeftChild():
                    current_node.parent.leftChild = current_node.rightChild
                    current_node.rightChild.parent = current_node.parent
                elif current_node.isRightChild():
                    current_node.parent.rightChild = current_node.rightChild
                    current_node.rightChild.parent = current_node.parent
                else:
                    current_node.root = current_node.rightChild
                    current_node.rightChild.parent = None



    def inOrderTraversal(self, root):
        if root != None:
            self.inOrderTraversal(root.getLeftChild())
            print(root.getKey())
            self.inOrderTraversal(root.getRightChild())


mytree = BinarySearchTree()
mytree.put(20,'red')
mytree.put(10,'blue')
mytree.put(25,'yellow')
mytree.put(30,'at')
mytree.put(22,'abc')
mytree.put(50,'def')
mytree.put(15,'thr')



mytree.inOrderTraversal(mytree.root)
print("\n")
mytree.delete(10)
#print(mytree.size)
mytree.inOrderTraversal(mytree.root)

#print(mytree.get(6))

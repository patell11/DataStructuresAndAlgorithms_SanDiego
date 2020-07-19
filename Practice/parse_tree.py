from tree import BinaryTree
from stack import Stack
import operator

def buildParseTree(exp):
    exp_lst = exp.split()
    root_node = BinaryTree(" ")
    current_node = root_node
    parent_stack = Stack()
    parent_stack.push(root_node)


    for e in exp_lst:
        if e in ['(']:
            current_node.insertLeft(' ')
            parent_stack.push(current_node)
            current_node = current_node.getLeftChild()
        elif e in ['+','-','*','/']:
            current_node.setRootVal(e)
            current_node.insertRight(' ')
            parent_stack.push(current_node)
            current_node = current_node.getRightChild()
        elif e in [')']:
            current_node = parent_stack.pop()

        elif e not in ['+','-','*','/','(',')']:
            try:
                current_node.setRootVal(int(e))
                current_node = parent_stack.pop()
            except ValueError:
                raise ValueError("token '{}' is not a valid number".format(e))

    return current_node

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


def printExp(tree):
    exp = ""
    if tree:
        """
            if the left and right of the tree does not exist we use the extra condition to avoid the extra brackets around
            operands
        """
        if tree.getLeftChild():
            exp = '(' + printExp(tree.getLeftChild())
        else:
            exp = printExp(tree.getLeftChild())

        exp = exp + str(tree.getRootVal())

        if tree.getRightChild():
            exp = exp + printExp(tree.getRightChild()) + ')'
        else:
            exp = exp + printExp(tree.getRightChild())

    return exp


# def evaluate(tree):
#     opers = {'+': operator.add, '-': operator.sub, '/': operator.truediv, '*': operator.mul}
#     leftChild = tree.getLeftChild()
#     rightChild = tree.getRightChild()
#
#     if leftChild and rightChild:
#         fn = opers[tree.getKey()]
#         return fn(evaluate(leftChild), evaluate(rightChild))
#     else:
#         return int(tree.getKey())


def evaluate2(tree):
    opers = {'+': operator.add, '-': operator.sub, '/': operator.truediv, '*': operator.mul}
    leftChild = tree.getLeftChild()
    rightChild = tree.getRightChild()

    if leftChild == None and rightChild == None:
        return int(tree.getRootVal())

    fn = opers[tree.getRootVal()]
    return fn(evaluate2(leftChild), evaluate2(rightChild))


pt = buildParseTree("( 3 + ( 4 * 5 ) )")     #("( ( 10 + 5 ) * 3 )")   #
postorder(pt)
print("------>")
print(printExp(pt))
print(evaluate2(pt))
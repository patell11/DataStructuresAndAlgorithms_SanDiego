from tree import BinaryTree
from stack import Stack

def buildParseTree(exp):

    exp = exp.split()
    tree = BinaryTree("")
    parent_stack = Stack()
    parent_stack.push(tree)
    current_node = tree

    for i in exp:
        if i == '(':
            current_node.insertLeft("")
            parent_stack.push(current_node)
            current_node = current_node.getLeftChild()

        elif i in ['*', '/', '+', '-']:
            current_node.setRootVal(i)
            current_node.insertRight("")
            parent_stack.push(current_node)
            current_node = current_node.getRightChild()

        elif i == ')':
            current_node = parent_stack.pop()

        elif i not in [')', '*', '+', '/', '-', '(']:
            current_node.setRootVal(i)
            parent = parent_stack.pop()
            current_node = parent

        #print(parent_stack.size())

    return tree



def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getKey())

def printExp(tree):
    exp = ""
    if tree:
        """
            if the left and right of the tree does not exit we use the extra condition to avoid the extra brackets around
            operands
        """
        if tree.getLeftChild():
            exp = '(' + printExp(tree.getLeftChild())
        else:
            exp = printExp(tree.getLeftChild())

        exp = exp + str(tree.getKey())

        if tree.getRightChild():
            exp = exp + printExp(tree.getRightChild()) + ')'
        else:
            exp = exp + printExp(tree.getRightChild())

    return exp

import operator
def evaluate(tree):
    opers = {'+': operator.add, '-': operator.sub, '/': operator.truediv, '*': operator.mul}
    leftChild = tree.getLeftChild()
    rightChild = tree.getRightChild()

    if leftChild and rightChild:
        fn = opers[tree.getKey()]
        return fn(evaluate(leftChild), evaluate(rightChild))
    else:
        return int(tree.getKey())



pt = buildParseTree("( 3 + ( 4 * 5 ) )")     #("( ( 10 + 5 ) * 3 )")   #
postorder(pt)
print("------>")
print(printExp(pt))
print(evaluate(pt))
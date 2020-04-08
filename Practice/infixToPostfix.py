from stack import Stack

def infixToPostfix(infixexp):
    opstack = Stack()

    infixexplist = list(infixexp.split())
    postfixList = list()
    for exp in infixexplist:
        if exp in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or exp in "0123456789":
            postfixList.append(exp)
        elif exp == "(" :
            opstack.push(exp)
        elif exp == ")":
            top = opstack.pop()
            while top != "(":
                postfixList.append(top)
                top = opstack.pop()
        else:
            if opstack.isEmpty():
                opstack.push(exp)
            else:
                while precedence(opstack.peek2(), exp) and not opstack.isEmpty():
                    top = opstack.pop()
                    postfixList.append(top)
                opstack.push(exp)
    while not opstack.isEmpty():
        postfixList.append(opstack.pop())

    return " ".join(postfixList)


def precedence(s1, s2):
    #print("comparing " + s1 + " and " + s2)
    dictPrec = {"/":3, "*":3, "+":2, "-":2, "(":1, "na":0}
    precVal1 = dictPrec[s1]
    precVal2 = dictPrec[s2]
    if precVal1 >= precVal2:
        return True
    else:
        return False

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

def postfixEval(postfixExp):

    postfixExpList = list(postfixExp.split())
    operandStack = Stack()

    for exp in postfixExpList:
        if exp in "0123456789":
            operandStack.push(int(exp))
        else:
            if operandStack.isEmpty():
                print("No operands to compute on")
            else:
                opr2 = operandStack.pop()
                opr1 = operandStack.pop()
                output = doMath(opr1, opr2, exp)
                operandStack.push(output)
    return operandStack.pop()


def doMath(op1, op2, op):
    if op == "/":
        return op1 / op2
    elif op == "*":
        return op1 * op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))



import sys

class Bracket:
    def __init__(self, position, bracket):
        self.bracket = bracket
        self.position = position

def matching(char1, char2):
    return (char1 + char2) in ["()", "{}", "[]"]

def checkMisMatch(text):
    open_brackets_stack = []
    for index, char in enumerate(text, start = 1):
        if char in "[{(":
            value = Bracket(index, char)
            open_brackets_stack.append(value)

        elif char in "]})":
            if not open_brackets_stack:
                return index
            top = open_brackets_stack.pop()
            if not matching(top.bracket, char):
                return index

    if open_brackets_stack:
        top = open_brackets_stack.pop()
        return top.position

    return "Success"


if __name__ == '__main__':
    text = input().strip("\n")
    print(checkMisMatch(text))
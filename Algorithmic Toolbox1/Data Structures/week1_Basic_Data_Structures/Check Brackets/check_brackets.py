# python3

from collections import namedtuple
import sys

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for index, character in enumerate(text, start = 1):
        if character in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(character, index))


        if character in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return index
            top = opening_brackets_stack.pop()
            if not are_matching(top.char,character):
                return index

    if opening_brackets_stack:
        top = opening_brackets_stack.pop()
        return top.position

    return "Success"

# for text,answer in (
#         ("[]","Success"),
#         ("{}[]","Success"),
#         ("[()]", "Success"),
#         ("(())","Success"),
#         ("{[]}()","Success"),
#         ("{","1"),
#         ("{[}",3),
#         ("foo(bar)","Success"),
#         ("foo(bar[i)","10"),
# ):
#     print(find_mismatch(text),answer)


if __name__ == "__main__":
    text =  sys.stdin.read().strip("\n")
    print(find_mismatch(text))

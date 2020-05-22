#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

maximum = 4294967296
minimum = -4294967296

def IsBinarySearchTree(tree):
  # Implement correct algorithm here

  return check(0, tree, minimum, maximum)



def check(index, tree, minimum, maximum):
  ## If lenght is zero its a BST

  if len(tree) == 0:
    return True

  if index == -1:
    return True

  if tree[index][0] < minimum or tree[index][0] > maximum or tree[index][0] == maximum:
    return False

  return (check(tree[index][1], tree, minimum, tree[index][0]) and check(tree[index][2], tree, tree[index][0], maximum))



def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()

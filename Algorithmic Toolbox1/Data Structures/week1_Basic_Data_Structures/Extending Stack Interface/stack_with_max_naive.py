#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.maximum = None

    def Push(self, a):
        if (not self.__stack):
            self.__stack.append(a)
            self.maximum = a
        elif (a > self.maximum):
            temp = 2*a - self.maximum
            self.__stack.append(temp)
            self.maximum = a
        else:
            self.__stack.append(a)


    def Pop(self):
        if not self.__stack:
            return

        top = self.__stack[-1]
        if top > self.maximum:
            self.maximum = 2*self.maximum - top
            self.__stack.pop()
        else:
            self.__stack.pop()


    def Max(self):
        assert(len(self.__stack))
        return self.maximum

    def print_stack(self):
        return self.__stack


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(input()) #int(sys.stdin.readline())
    for _ in range(num_queries):
        query = input().split() #sys.stdin.readline().split()

        #print(stack.print_stack())
        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
        #print(stack.print_stack())

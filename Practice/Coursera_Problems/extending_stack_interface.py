

class StackExtended:
    def __init__(self):
        self.stack = []
        self.maximum = None

    def push(self, val):
        if not self.stack:
            self.stack.append(val)
            self.maximum = val
        elif val > self.maximum:
            self.stack.append(2*val - self.maximum)
            self.maximum = val
        else:
            self.stack.append(val)

    def pop(self):
        if not self.stack:
            return
        top = self.stack[-1]
        if top > self.maximum:
            self.maximum = 2*self.maximum - top
            self.stack.pop()
        else:
            self.stack.pop()


    def get_max(self):
        return self.maximum


if __name__ == '__main__':
    stack = StackExtended()
    n_input = int(input())
    for i in range(n_input):
        operation = input().split()
        if operation[0] == 'push':
            stack.push(int(operation[1]))
        elif operation[0] == 'pop':
            stack.pop()
        elif operation[0] == 'max':
            print(stack.get_max())

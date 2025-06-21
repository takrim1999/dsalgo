class stack:
    def __init__(self):
        self.stack = []
        self.top = 0

    def push(self, value):
        self.stack[:self.top] = value


myStack = stack()
myStack.push(15)
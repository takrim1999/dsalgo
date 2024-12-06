class Stack:
    def __init__(self,size=8):
        self.size = size
        self.i = 0
        self.array = [None]*size

    def is_empty(self):
        if self.i == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.i+1==self.size:
            return True

    def push(self,element):
        if self.is_full():
            print("stack overflowed")
        else:
            self.array[self.i] = element
            self.i+=1

    def pop(self):
        self.array[self.i]=None
        self.i-=1
    
    def __str__(self):
        return ",".join([str(k) for k in self.array[:self.i]])  # Only High level property I'm using cause it is not the property of stack.
    
########## To Test ##########
# new = Stack()
# print(new)
# print(new.is_empty())
# new.push(5)
# new.push(12)
# new.push(35)
# print(new)
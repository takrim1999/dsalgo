# In python there is no builtin data structure as array
# So, Array should be created, here we are gonna use a module.
# I'm going to create a class named Array and making all the operation like C program


class Array:
    def __init__(self, type: str, size: int, elements=None):
        self.start = 0
        self.end = -1
        self.size = size
        self.type = type
        self.mainarray = ["None"] * size
        if elements:
            for i in range(self.size):
                if i == len(elements):
                    break
                self.end += 1
                self.mainarray[self.end] = elements[i]

    # 1. Traverse
    def printArray(self):
        point = 0
        while point <= self.end:
            print(self.mainarray[point])
            point += 1

    # 2. Access element with index
    def printElement(self, index):
        if index <= self.end:
            print(self.mainarray[index])
        else:
            print("index out of range")

    # 3. Pushing a element at the end of array
    def pushLast(self, el):
        if self.end < self.size - 1:
            self.end += 1
            self.mainarray[self.end] = el
        else:
            print("Array is Full")

    # 4. Inserting an element at start of the array
    def pushFirst(self, el):
        if self.size - 1 == self.end:
            print("Array is full")
        else:
            point = 0
            while point < self.end:
                temp = self.mainarray[point + 1]
                self.mainarray[point + 1] = self.mainarray[point]
                point += 1

    # 5. inserting at any point of array
    def insertItem(self, index, el):
        if self.end < self.size - 1:
            self.end += 1
        point = index
        while point <= self.end:
            temp = self.mainarray[point + 1]
            self.mainarray[point + 1] = self.mainarray[point]
            self.mainarray[point] = temp
            point += 1
        self.mainarray[index] = el

    # 7. Deleting an element by index

    def deleteItem(self, index):
        deleted = self.mainarray[index]
        while index <= self.end:
            self.mainarray[index] = self.mainarray[index + 1]
            index += 1
        self.end -= 1


arr1 = Array("str", 8, [1, 2, 3, 4, 5])
# arr1.printArray()
arr1.pushLast(9)
arr1.printArray()
# arr1.printElement(4)
# arr1.printArray()
arr1.deleteItem(2)
# # arr1.insertItem(3, 25)
arr1.printArray()

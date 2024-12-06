class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self,data):
        node = Node(data = data)
        node.next =  self.head
        self.head = node

    def insertAtEnd(self,data):
        node = Node(data=data)
        data = self.head
        while data.next!=None:
            data = data.next
        data.next = node

    def popItem(self):
        if self.head == None:
            print("List empty")
        else:
            data = self.head
            self.head = data.next
    
    def dequeueItem(self):
        if self.head == None:
            print("List empty")
        else:
            data = self.head
            while data.next != None:
                data = data.next
            data=None

    def printList(self):
        data = self.head
        if data==None:
            print("List is empty!")
        while data!=None:
            print(data.data)
            data = data.next


myList = LinkedList()
myList.printList()
myList.insertAtBegining(5)
myList.insertAtBegining(4)
myList.insertAtBegining(3)
myList.insertAtEnd(6)
myList.printList()
myList.popItem()
myList.printList()
myList.dequeueItem()
myList.printList()

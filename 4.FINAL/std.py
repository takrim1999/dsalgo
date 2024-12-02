def makeCompatible(num):    
    if len(str(num))<2:
        return "0" + str(num)
    else:
        return str(num)

class Student:    
    def __init__(self,name=None,roll=None,age=None,cgpa=None,position=None):
        self.name = name
        self.roll = roll
        self.age = age
        self.cgpa = cgpa
        self.position = position
        if self.name and self.roll:
            self.generateId()
            self.incrementCount()
            pass
        else:
            self.setInfo()
            self.incrementCount()
    
    def setInfo(self):
        self.name = input("Name: ")
        self.roll = input("Class Roll: ")
        self.age = input("Age: ")
        self.cgpa = input("CGPA: ")
        self.position = input("Result Position: ")
        if self.name and self.roll:
            self.generateId()
    
    def generateId(self):
        self.getCount()
        self.id = f"{makeCompatible(self.count)}{self.name[0].lower()}{makeCompatible(self.roll)[-2]}{self.name[-1].lower()}{makeCompatible(self.roll)[-1]}"

    def getCount(self):
        with open("counter.number",'r') as counter:
            self.count = int(counter.read().strip())
    
    def incrementCount(self):
        self.count += 1
        with open("counter.number","w") as counter:
            counter.write(str(self.count))
    
    def getInfo(self):
        return {self.id : {'name': self.name, 'roll': self.roll, 'age':self.age, 'cgpa':self.cgpa, 'position': self.position}}
        print("Secret ID: ", self.id)
        print("Student Roll: ",self.roll)
        print("Student Name: ",self.name)
        print("Student Age: ",self.age)
        print("Student CGPA: ",self.cgpa)
        print("Student Position: ", self.position)

    def __str__(self):
        
        return f"<Student: {self.name}>"
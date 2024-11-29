import json

count = 1

DATABSE_NAME = "objectDb.record"

def makeCompatible(num):
    if len(str(num))<2:
        return "0" + str(num)
    else:
        return str(num)

class Student:
    
    def __init__(self):
        pass
    
    def setInfo(self):
        self.roll = input("Input Roll: ")
        self.name = input("Input Name: ")
        global count
        self.id = f"{makeCompatible(count)}{name[0].lower()}{makeCompatible(roll)[0]}{name[-1].lower()}{makeCompatible(roll)[1]}"
        count += 1                
        print(f"Informations for {self.name}")
        print(f"Roll: {self.roll}")
        self.age = input("Input Age: ")
        self.cgpa = input("Input CGPA: ")
        self.position = input("Input Position: ")
        data = {self.id:{"name":self.name, "roll":self.roll, "age": self.age, "cgpa": self.cgpa, "position" : self.position}}
        with open(DATABSE_NAME,"a") as database:
            database.write(str(data)+"\n")
    
    def showInfo(self):
        with open(DATABSE_NAME,"r") as database:
            records = database.read()
        # print("Name: ")
        # print("Roll: ")
        # print("Age: ")
        print(records)


# student = Student(input("Class Roll: ")," ".join([i.capitalize() for i in input("Name: ").split(" ")]))
# print(student.setInfo())
# student.showInfo(student.id)
# student_record = {}
# records = []

######### Setting Batch Info #########
# with open("icestudents.db","r") as source:
#     lines = source.read().split("\n")
# for record in lines:
#     if record:
#         roll,name = record.split(',')
#         myStudent = Student(roll," ".join([i.capitalize() for i in name.split(" ")]))
#         myStudent.setInfo()
# for record in lines:
#     print(record)
        # print(i)

import os
import std
class StudentRecord:
    def __init__(self):
        self.studentList = []
        with open('objectDb.record', 'r') as database:
            data  = database.read().split('\n')[:-1]
            for record in data:
                self.studentList.append(eval(record))
    
    def searchStudent(self,parameter):
        os.system("clear")
        if parameter == "name":
            name = input("Query Name: ")
            payload = []
            for record in self.studentList:
                for id, data in record.items():
                    if name.lower() in data['name'].lower():
                        payload.append(data)
            if not payload:
                payload.append({'error': "No record found!"})
            return payload
        if parameter == "cgpa":
            payload = []
            cgpaquery = input("CGPA query([>,<,>=,<=,==]cgpa): ")
            if ">=" in cgpaquery:
                cg = float(cgpaquery.replace(">=",''))
                for record in self.studentList:
                    for id, data in record.items():
                        if data['cgpa'] != 'NA' and float(data['cgpa'])>=cg:
                            payload.append(data)
            elif "<=" in cgpaquery:
                cg = float(cgpaquery.replace("<=",''))
                for record in self.studentList:
                    for id, data in record.items():
                        if data['cgpa'] != 'NA' and float(data['cgpa'])<=cg:
                            payload.append(data)
            elif "<" in cgpaquery:
                cg = float(cgpaquery.replace("<",''))
                for record in self.studentList:
                    for id, data in record.items():
                        if data['cgpa'] != 'NA' and float(data['cgpa'])<cg:
                            payload.append(data)
            elif ">" in cgpaquery:
                cg = float(cgpaquery.replace(">",''))
                for record in self.studentList:
                    for id, data in record.items():
                        if data['cgpa'] != 'NA' and float(data['cgpa'])>cg:
                            payload.append(data)
            elif "==" in cgpaquery:
                cg = float(cgpaquery.replace("==",''))
                for record in self.studentList:
                    for id, data in record.items():
                        if data['cgpa'] != 'NA' and float(data['cgpa'])==cg:
                            payload.append(data)
            if not payload:
                payload.append({'error': "No record found!"})
            
            return payload
        
    def addStudent(self):
        student = std.Student()
        self.studentList.append(student.getInfo())
        with open('objectDb.record', 'w') as database:
            for i in self.studentList:
                database.write(str(i)+"\n")        
        return student.getInfo()
                
def display():
    os.system("clear")
    choice = input('''Welcome to ICE student Database!
    type "exit" to exit
    type "search" to search in database
    type "add" to add record
    type "edit" to edit a record!
> ''')
    return choice


while True:
    choice = display()
    myRecord = StudentRecord()
    if choice == "exit":
        break
    elif choice == "search":
        parameter = input("Search parameter(roll,name,cgpa,position,age): ")
        messages = myRecord.searchStudent(parameter)
        for message in messages:
            print(message)
        while input("Search again?\n>") == "yes":
           messages = myRecord.searchStudent(parameter)
           for message in messages:
               print(message)
        else:
            pass
    elif choice == 'add':
        messages = []
        messages.append({'New Record Added' : myRecord.addStudent()})
        while input("Add more?\n>") == "yes":
            messages.append({'New Record Added' : myRecord.addStudent()})
        for message in messages:
            print(message)
    # elif choice == "edit":
        

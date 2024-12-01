# def makeCompatible(num):    
#     if len(str(num))<2:
#         return "0" + str(num)
#     else:
#         return str(num)
import os

class StudentRecord:
    def __init__(self):
        self.studentList = []
        with open('objectDb.record', 'r') as database:
            data  = database.read().split('\n')[:-1]
            for record in data:
                self.studentList.append(eval(record))
    
    def searchStudent(self,parameter=None):
        os.system("clear")
        if not parameter:
            parameter = input("Search parameter(roll,name,cgpa,position,age): ")
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
        messages = myRecord.searchStudent()
        for message in messages:
            print(message)
        while input("Search again?: ") == "yes":
           messages = myRecord.searchStudent('cgpa')
           for message in messages:
               print(message)
        else:
            pass
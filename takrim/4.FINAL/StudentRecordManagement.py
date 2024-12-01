# def makeCompatible(num):    
#     if len(str(num))<2:
#         return "0" + str(num)
#     else:
#         return str(num)
    

class Manage:
    def __init__(self):
        self.studentList = []
        with open('objectDb.record', 'r') as database:
            data  = database.read().split('\n')[:-1]
            for record in data:
                self.studentList.append(eval(record))
    
    def searchStudent(self,id=None):
        parameter = input("Search parameter(roll,name,cgpa,position,age): ")
        if parameter == "name":
            name = input("Query Name: ")
            for record in self.studentList:
                for id, data in record.items():
                    if name.lower() in data['name'].lower():
                        print(data)
        if parameter == "cgpa":
            cgpaquery = input("query: ")
            if "<" in cgpaquery:
                cg = float(cgpaquery.replace("<",''))
                for record in self.studentList:
                    for id, data in record.items():
                        if data['cgpa'] != 'NA' and float(data['cgpa'])<cg:
                            print(data)
                


# s1 = Student("Md. Takrim Ul Alam",1911177149,25,3.3,20)
# s2 = Student()
# s1.getInfo()
# s2.getInfo()
management = Manage()
management.searchStudent()
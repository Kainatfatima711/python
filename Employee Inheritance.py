# Parent Classs
class Person():  # WHERE ANY PERSON IS AN EMPLOYEE OF A COMPANY


    def __init__(self , name , idnumber):
            self.name = name
            self.idnumber = idnumber

    def display(self):
            print(self.name)
            print(self.idnumber)


#Child Class
class Employee(Person):
       def __init__(self , name , idnumber , salary , post):
              
            
            self.salary = salary
            self.post = post
            super().__init__( name , idnumber)


myEmployee = Employee("Rahul" , 886012 , 200000 , "Intern")

myEmployee.display()


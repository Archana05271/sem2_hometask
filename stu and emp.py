
#1
class Person:
    def
    name(self):
        self.name = input("Enter the name of the Student: ")

    def show_name(self):
        print("The Student_Name is:", self.name)

class Student(Person):
    def student_id(self):
        self.stu_id = input("Enter the student ID: ")

    def show_student_id(self):
        print("The Student_ID is:", self.stu_id)

stu = Student()
stu.name()
stu.student_id()
stu.show_name()
stu.show_student_id()
#2
class Employee:
    def info(self):
        self.name = input("Enter the name of the employee: ")
        self.salary = int(input("Enter the salary of the employee: "))

class Manager(Employee):
    def dept(self):
        self.depart = input("Enter the department name: ")

    def display(self):
        self.info()
        self.dept()
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.depart)

emp = Manager()
emp.display()

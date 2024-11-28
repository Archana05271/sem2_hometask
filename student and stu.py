#student details
class Student:
    def __init__(self, name, rollno, mark1, mark2, mark3, mark4, mark5):
        self.name = name
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.mark4 = mark4
        self.mark5 = mark5
    
    def calculate_per(self):
        total = self.mark1 + self.mark2 + self.mark3 + self.mark4 + self.mark5
        per = (total / 500) * 100 
        return per
    
    def display(self):
        per = self.calculate_per()
        grade = self.grade()  
        print(f"\nName: {self.name}")
        print(f"Roll Number: {self.rollno}")
        print(f"Subject 1: {self.mark1}")
        print(f"Subject 2: {self.mark2}")
        print(f"Subject 3: {self.mark3}")
        print(f"Subject 4: {self.mark4}")
        print(f"Subject 5: {self.mark5}")
        print(f"Percentage: {per}%")
        print(f"Grade: {grade}")
    
    def grade(self):
        per = self.calculate_per()
        if per >= 85:
            return "S"
        elif per >= 75:
            return "A"
        elif per >= 65:
            return "B"
        elif per >= 55:
            return "C"
        else:
            return "D"
        
# Creating an object of the Student class
stu = Student("Anjana", "54", 90, 99, 89, 80, 85)
stu.display()
#student
class Student: 
    def __init__(self,name,age,course,grade): 
        self.name=name 
        self.age=age 
        self.course=course 
        self.grade=grade 
        print(f"Student for {self.name} is created.") 
    def show(self): 
        print(f"Name:{self.name}\nAge:{self.age}\nCourse:{self.course}\nGrade:{self.grade}") 
    def __del__(self): 
        print(f"Student  for {self.name} is  deleted.") 
 
stu=Student("Anjana",18,"AI","S") 
stu.show() 
del stu

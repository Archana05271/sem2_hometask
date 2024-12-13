import random 
class Students:
    grades = [f"{i}th Grade" for i in range(1, 13)]  # List of valid grades
    
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = namew
        self.grade = grade
    def gen_rand_id(self):
        'st_id = random.randint(1000, 9999)
        return f"STU{st_id}"
    def Validatedetails(self):
        if not self.student_id.startswith("STU") or not self.student_id[3:7].isdigit():
            print("Student ID must be in the format STU1234.")
            return False
        if len(self.name) < 2 or not all(i.isalpha() or i.isspace() for i in self.name):
            print("Name of the student must be at least two characters and contain alphabets and spaces only.")
            return False
        if self.grade not in Students.grades:
            print("Grades must follow the format <number>th Grade.")
            return False
        print("Details Are Valid!!")                        
        return True

    def display_details(self):
        print("\nStudent Details:")
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.name}")
        print(f"Student Grade: {self.grade}")
ID = input("Enter ID (or leave empty to generate a random ID): ")
Name = input("Enter name: ")
Grade = input("Enter Grade (e.g., 1st Grade): ")

if not ID:
    stu = Students("TEMP", Name, Grade)  
    ID = stu.gen_rand_id() 
stu= Students(ID, Name, Grade)

if stu.Validatedetails():  
    stu.display_details()

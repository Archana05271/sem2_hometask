
#1
class Camera: 
    def __init__(self): 
        self.resolution = input("Enter the camera resolution (e.g., 1080p): ") 
        self.camera_name = input("Enter the camera name: ") 
    def display_camera_details(self): 
        print("Camera Resolution:", self.resolution) 
        print("Camera Name:", self.camera_name) 

class Phone: 
    def __init__(self): 
        self.phone_number = input("Enter the phone number (e.g., 123-456-7890): ") 
    def display_phone_details(self): 
        print("Phone Number:", self.phone_number)

class SmartPhone(Camera, Phone): 
    def __init__(self): 
        # Initialize parent classes
        Camera.__init__(self) 
        Phone.__init__(self) 
        self.brand = input("Enter the smartphone brand: ") 
        self.model = input("Enter the smartphone model: ") 
    def display_device_details(self): 
        print("\nSmartphone Details:")
        print("Brand:", self.brand) 
        print("Model:", self.model)
        self.display_camera_details() 
        self.display_phone_details()
smartphone = SmartPhone()
smartphone.display_device_details()
#2
class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
    def student_info(self):
        print("Student Name:", self.name)
        print("Course:", self.course)
        
class StudentAthlete(Student):
    def __init__(self, name, course, sport_name):
        super().__init__(name, course)  
        self.sport_name = sport_name
    def display_athlete_info(self):
        self.student_info()  
        print("Sport:", self.sport_name) 
athlete = StudentAthlete("Akshay", "Computer Science", "Soccer")
athlete.display_athlete_info()

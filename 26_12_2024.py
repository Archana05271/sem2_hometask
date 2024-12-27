class Calculator: 
    def __init__(self, num1, num2): 
        self.num1 = num1 
        self.num2 = num2
    def perform_operation(self): 
        if not isinstance(self.num1, int) or not isinstance(self.num2, int): 
            raise ValueError("Both numbers should be integers. Please try again.") 
        else:
            if operation_choice > 4 or operation_choice < 1:
                raise KeyError("Invalid choice. Please select a number between 1 and 4.")
            else:
                match operation_choice: 
                    case 1: 
                        return self.num1 + self.num2
                    case 2: 
                        return self.num1 - self.num2  
                    case 3: 
                        return self.num1 * self.num2
                    case 4: 
                        if self.num2 == 0: 
                            raise ZeroDivisionError("Cannot divide by zero.")
                        else: 
                            return self.num1 / self.num2  
try: 
    while True: 
        print("Choose an operation: 1 ,2,3,4")
        operation_choice = int(input("Enter your choice: ")) 
        num1 = int(input("Enter the first number: ")) 
        num2 = int(input("Enter the second number: ")) 
        calculator = Calculator(num1, num2) 
        result = calculator.perform_operation() 
        print("The result is:", result) 
except ValueError as e: 
    print(e) 
except KeyError as e: 
    print(e) 
except ZeroDivisionError as e: 
    print(e)

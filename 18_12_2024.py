class Calculator:
    def calculate(self, a, b=0, c=0):
        for i in (a, b, c):
            if type(i) not in (int, float):
                raise ValueError("All arguments must be either integers or floats.")
        if a != 0 and b != 0 and c != 0:
            return a * b * c
        elif a != 0 and b != 0 and c == 0:
            return a + b
        elif a != 0 and b == 0 and c == 0:
            return a ** 2
        else:
            raise ValueError("Invalid combination of arguments.")

a = Calculator()
print(a.calculate(2))  
print(a.calculate(2, 3))  
print(a.calculate(2, 3, 4))
try: 
    print(c.calculate(2, 3, "4"))   
except ValueError as e: 
    print(f"Error: {e}")

class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def displayVehicleInfo(self):
        print(f"Make:{self.make}\nModel:{self.model}\nYear:{self.year}")
class Car(Vehicle):
    def __init__(self,make,model,year,no_of_doors,trunk_capacity):
        Vehicle.__init__(self,make,model,year)
        self.no_of_doors=no_of_doors
        self.trunk_capacity=trunk_capacity
    def displayCarInfo(self):
        print(f"Number of doors:{self.no_of_doors}\nTrunk Capacity:{self.trunk_capacity}")
class Truck(Vehicle):
    def __init__(self,make,model,year,cargo_capacity,no_of_axles):
        Vehicle.__init__(self,make,model,year)
        self.cargo_capacity=cargo_capacity
        self.no_of_axles=no_of_axles
    def displayTruckInfo(self):
        print(f"Cargo Capacity:{self.cargo_capacity}\nNumber of axles:{self.no_of_axles}")
class PickupTruck(Car,Truck):
    def __init__(self,make,model,year,no_of_doors,trunk_capacity,cargo_capacity,no_of_axles):
        Car.__init__(self,make,model,year,no_of_doors,trunk_capacity)
        Truck.__init__(self,make,model,year,cargo_capacity,no_of_axles)
    def display(self):
        self.displayVehicleInfo()
        self.displayCarInfo()
        self.displayTruckInfo()
p=PickupTruck("Toyota","T-50",2024,4,"2000litres","1000 litres",2)
p.display()

class Product:
    def __init__(self,prod_Id,prod_name,pro_price):
        self.prod_Id=prod_Id
        self.prod_name=prod_name
        self.prod_price=pro_price
    def displayProductInfo(self):
        print(f"Product Id:{self.prod_Id}\nProduct Name:{self.prod_name}\nProduct Price:{self.prod_price}")
class Electronics(Product):
    def __init__(self,prod_Id,prod_name,prod_price,warranty,brand):
        Product.__init__(self,prod_Id,prod_name,prod_price)
        self.warranty=warranty
        self.brand=brand
    def displayElectronicsInfo(self):
        self.displayProductInfo()
        print(f"Warranty Year:{self.warranty}\nBrand Name:{self.brand}")
class Clothing(Product):
    def __init__(self,prod_Id,prod_name,prod_price,size,material):
        Product.__init__(self,prod_Id,prod_name,prod_price)
        self.size=size
        self.material=material
    def displayClothingInfo(self):
        self.displayProductInfo()
        print(f"Size:{self.size}\nMaterial:{self.material}")
ele=Electronics("Galaxy"," Phone","450","3 years","Samsung")
ele.displayElectronicsInfo()
clo=Clothing("Kasuthri","Kurti",500,"M","Silk")
clo.displayClothingInfo()

#1LIBRARY
class Library: 
    def __init__(self,lib_name,lib_address): 
        self.lib_name=lib_name 
        self.lib_address=lib_address 
    def displayLibraryinfo(self): 
        print(f"Name of Library:{self.lib_name}\nLibrary Address:{self.lib_address}") 
class Members: 
    def __init__(self,mem_name,mem_contact): 
        self.mem_name=mem_name 
        self.mem_contact=mem_contact 
    def displayMembersinfo(self): 
        print(f"Name of Member:{self.mem_name}\nMember Contact:{self.mem_contact}") 
class LibraryManagement(Library,Members): 
    def __init__(self,lib_name,lib_address,mem_name,mem_contact): 
        super().__init__(lib_name,lib_address) 
        Members.__init__(self,mem_name,mem_contact) 
    def display(self): 
        self.displayLibraryinfo() 
        self.displayMembersinfo() 
l=LibraryManagement("NATIONAL LIBRARY","KOLLENCODE STREET","AMAL",6238820605) 
l.display()
#2Food
class Restaurant: 
    def __init__(self,Rest_name,Items): 
        self.Rest_name=Rest_name 
        self.Items=Items 
    def displayrestaurantInfo(self): 
        print(f"Name of the Restaurant:{self.Rest_name}\nFood Available:{self.Items}") 
class Delivery: 
    def __init__(self,Deli_name,Deli_contact): 
        self.Deli_name=Deli_name 
        self.Deli_contact=Deli_contact 
    def displaydelieryinfo(self): 
        print(f"Name of the delivery Boy:{self.Deli_name}\nBoy's COntact:{self.Deli_contact}") 
class Order(Restaurant,Delivery): 
    def __init__(self,Rest_name,Items,Deli_name,Deli_contact): 
        super().__init__(Rest_name,Items) 
        Delivery.__init__(self,Deli_name,Deli_contact) 
    def display(self): 
        self.displayrestaurantInfo() 
        self.displaydelieryinfo() 
Delivery=Order("Kumar Cafe","Parotta,Beef Curry,Chicken 65","Ranjith",8945623147) 
Delivery.display()

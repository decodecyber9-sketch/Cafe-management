#Coffe management system using python oops
import random

class Coffee:
    def __init__(self):
        self.bill = 0
        self.available_tea = {"Capachino":12,
        "Brown Tea":10,
        "Coffee": 12}
    
    def show_menu(self):
        for key, value in self.available_tea.items():
            print(f"{key} : {value}")
            
    def place_order(self,tea):
        if tea in self.available_tea:
            self.bill += self.available_tea[tea]
            print(" Order placed✔️")
            print("Your bill now",self.bill)
        else:
            print("tea not found❌") 
    
    def __call__(self):
        n = self.bill    
            
class pay_bill(Coffee):
    
    def __init__(self, name, id, bill):
        self.name = name
        self.id = id
        self.bill = bill
        
    def pin(self, pin):
        pin =""
        for i in range(4):
            num = random.randint(0,9)
            pin += str(num)
        return pin 
           
    def show_pin(self, id_num):
        if id_num == self.id:
            print("your pin:... ")
            return self.pin(self.pin)
        else:
            print("Sorry wrong I'd number.. ")      

Hotel = Coffee()
print(" <--Menu:-->")
#Hotel.show_menu()


#print(Bill.bill)
print("1.Place your order \n2.Exit")
while True:
    choice = input("Enter your choice: ")
    if choice == "1":
        Hotel.show_menu()
        tea = input("Enter tea (1,2,3): ")
        
        if tea == "1":
            Hotel.place_order("Capachino")
            
        elif tea == "2":
            Hotel.place_order("Brown Tea")
            
        elif tea == "3":
            Hotel.place_order("Coffee")  
        else:
    
            print("Sorry choose between(1,2,3)❌")     
    elif choice == "2":
        print("Good bye sir have a nice day🥰")
        break 
        
    else:
        print("Please chooses between 1 and 2")
        
Bill = pay_bill("sumair", 123, Hotel.bill)
print(f"{Bill.bill}$ ")

ID = input("Enter your I'd sir.. ")

if int(ID) == 123:
    Password = Bill.show_pin(int(ID))
    print(str(Password)) 
    pin = input("Enter your pin... ")
    
    if pin == Password:
        print("Bill paid successfully.. ")
    else:
        print("wrong password❌")    
    
else:
    print("wrong id sir... ")   
    
Bill.pin(1234)

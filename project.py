class Food:
    menu={
        "pizza": 10.00,
        "burger": 5.00,
        "chips": 2.00,
        "coke": 1.00,
        "water": 0.00,
  
    }
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.items =[]
        self.price = self.menu[name]
        self.quantity = 1
    
    def add(self, item):
        self.items.append(item)
        self.total += self.price
        self.quantity += 1
    def print_bill(self,tax,service):
        tax = (tax/100) * self.total
        service = (service/100) * self.total
        total = self.total + tax + service
        for item in self.items:
         
            print(f'{item:20}${self.menu[item]}')
        print(f"{'Total':20}{total:.2f}")
    def print_bills(self):
        print("Your bill is: ")
        for item in self.items:
            print(item)
        print(f"Your total is: {self.total}")
        print("Thank you for shopping with us!")
        print("Please come again!")
class User:
    def __init__(self,name,id,password,email):
        self.name=name
        self.id=id
        self.password=password
        self.email=email

    def showDetails(self):
        
        print(f"Name\t\t\t\t{self.name}")
        print(f"ID\t\t\t\t\t{self.id}")
        print(f"Password\t\t\t{self.password}")
        print(f"Email\t\t\t\t{self.email}")

class Bank(User):
    def __init__(self, name, id, password, email):
        super().__init__(name, id, password, email)
        self.Balance=0

    def Deposit(self,amount):
        self.deposit=amount
        self.Balance=self.Balance+self.deposit
        print(f"Your Balance Updated to {self.Balance}RS")

    def Withdraw(self,amount):
        self.withdraw=amount
        if (self.withdraw>self.Balance):
            print(f"Insufficient Balance || Availible Balance is {self.Balance}RS")
        else:    
            self.Balance=self.Balance-self.withdraw
            print(f"Your Remaining Balance is  {self.Balance}RS ")

    def showDetails(self):
        super().showDetails() 
        print(f"Availible Balance\t{self.Balance}RS") 

print()
print("\t\t\t\tDETAILS")
print("________________________________________________")

user1=Bank('Talha',220,'Talha123','Talha22@gmail.com')
user1.showDetails()
user1.Deposit(1000)
user1.Deposit(500)
user1.Withdraw(100)

print("_________________________________________________")

user2=Bank('Nabeed',221,'Nabeed123','Nabeed44@gmail.com')
user2.showDetails()
user2.Deposit(5000)
user2.Deposit(10000)
user2.Withdraw(2000)

print("_________________________________________________")

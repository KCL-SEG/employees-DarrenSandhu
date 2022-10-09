"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type = "", monthly_salary = 0, hours = 0, commisssion_contracts = 0, commission_bonus = 0, hourly_pay = 0, commission_hourly_pay = 0):
        self.name = name
        self.contract_type = contract_type
        self.monthly_salary = monthly_salary
        self.hours = hours
        self.commission_contracts = commisssion_contracts
        self.hourly_pay = hourly_pay
        self.commission_bonus = commission_bonus
        self.commission_hourly_pay = commission_hourly_pay
    
    def get_commision(self):
        if(self.commission_bonus != 0):
            return self.commission_bonus
        elif(self.commission_contracts != 0):
            return self.commission_contracts * self.commission_hourly_pay
        else:
            return 0

    def type_of_pay(self):
        if(self.contract_type == "Monthly"):
            return self.monthly_salary
        if(self.contract_type == "Hourly"):
            return self.hours * self.hourly_pay

    def get_pay(self):
        return self.type_of_pay() + self.get_commision()

    def __str__(self):
        if(self.contract_type == "Monthly"):
            if(self.commission_bonus > 0):
                return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a bonus commission {self.commission_bonus}. Their total pay is {self.get_pay()}."
            elif(self.commission_contracts > 0):
                return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a commission for {self.commission_contracts} contract(s) at {self.commission_hourly_pay}/contract. Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.get_pay()}."
        elif(self.contract_type == "Hourly"):
            if(self.commission_bonus > 0):
                return f"{self.name} works on a contract of {self.hours} hours at {self.hourly_pay}/hour and receives a bonus commission {self.commission_bonus}. Their total pay is {self.get_pay()}."
            elif(self.commission_contracts > 0):
                return f"{self.name} works on a contract of {self.hours} hours at {self.hourly_pay}/hour and receives a commission for {self.commission_contracts} contract(s) at {self.commission_hourly_pay}/contract. Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a contract of {self.hours} hours at {self.hourly_pay}/hour. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', contract_type = "Monthly", monthly_salary = 4000)
print(str(billie))
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', contract_type = "Hourly", hourly_pay = 25, hours = 100)
print(str(charlie))
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', contract_type = "Monthly", monthly_salary = 3000, commisssion_contracts = 4, commission_hourly_pay = 200)
print(str(renee))
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', contract_type = "Hourly", hourly_pay = 25, hours = 150, commisssion_contracts = 3, commission_hourly_pay = 220)
print(str(jan))
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', contract_type = "Monthly", monthly_salary = 2000, commission_bonus = 1500)
print(str(robbie))
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', contract_type = "Hourly", hourly_pay = 30, hours = 120, commission_bonus = 600)
print(str(ariel))

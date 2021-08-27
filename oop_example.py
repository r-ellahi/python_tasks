class Patient:
    def __init__(self, 
                name: str, 
                age: int, 
                height: float, 
                weight: float, 
                illness: str, 
                nhs_number: int,
                date_of_birth = "1/01/2000"
                ) -> None:
        
        self.name = name
        self.age = age
        self.height = height * 1.5
        self.weight = weight
        self.illness = illness
        self.bmi = self.height * weight
        self.dob = date_of_birth
        
        if nhs_number:
            self.nhs_number = nhs_number
            self.billing = False
        else:
            self.billing = True

        if self.bmi > 500:
            self.overweight = True
        else:
            self.overweight = False
            
    def update_weight(self, weight):
        self.weight = weight
        self.bmi = self.height * weight

        if self.bmi > 500:
            self.overweight = True
        else:
            self.overweight = False
            
    def discharge_patient(self):
        self.illness = None
        if self.billing:
            print("Your bill is £500")
            
patient_1 = Patient("Mr.Zero", 30, 185.0, 75.0, "Cold", 204845729)
patient_2 = Patient("Ms.Zero", 30, 160.0, 70.0, "Flu", None)
patient_3 = Patient("Harold", 45, 200.5, 800.9, "Broken Arm", 899093745734879)
patient_4 = Patient("Geraldine", None, 100, 50, "Broken Leg", None, "23/06/1965")

print(patient_3.bmi, patient_3.overweight)
patient_3.update_weight(1)
print(patient_3.bmi, patient_3.overweight)

patient_2.discharge_patient()
patient_3.discharge_patient()



# Example of Class - focus on encapsulation 
# only include the info needed for class
class Account():
    name = ""
    __balance = 0

    def deposit(self, amount):
        self.__balance += amount
        
    def get_balance(self):
        return self.__balance


deco_account = Account()
deco_account.name = "Deco"
money = deco_account.get_balance()
print(deco_account.get_balance())
money = 1000000000
print(deco_account.get_balance())
print(money)





#Abstraction Example - as long as data is retrieved, method does not matter
colour = ['purple', 'turquoise', 'green', 'red', 'blue', 'teal']
print(colour)
colour.sort()
print(colour)







# EXAMPLE OF INHERITANCE 
# class LeadDataEngineer(Employee) inherits all attributes from class Employee():
# additional attributes can be added to child (inherited) class that doesn't apply to parent class

class Employee():
    name = ""
    age = 0
    _salary = 40000
    
    def calculate_bonus(self):
        return self._salary / 10.0
    
    
class LeadDataEngineer(Employee):
    security_clearance = True
    
    def gives_raise(self, amount):
        self._salary += amount
    
    
oussama = LeadDataEngineer()
oussama.name = "Oussama"
oussama.gives_raise(3000)


dhanji = Employee()
dhanji.name = "Dhanji"



print(oussama.calculate_bonus())
print(dhanji.calculate_bonus())

# __attribute_name - private: cant be seen by anyone
# _attribute_name - protected: seen by class and students
# attribute_name - public: seen by the public



class My_Class():
    pass

c = My_Class()
print(dir(c))
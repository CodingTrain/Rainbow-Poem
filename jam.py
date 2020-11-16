class Person:
    ''' parent class'''

    def __init__(self, name, age, sector, yoe):
        self.name = name
        self.age = age
        self.sector = sector
        self. yoe = yoe


class Manager(Person):
    def duty(self):
        print(f"I'm {self.name} and my age is {self.age}")
        print("my duties are checking whether the employees do there job")


class Employee(Person):
    def duty(self):
        print(f"I'm {self.name} and my age is {self.age}")
        print("my duty to do job")


class Person_of_interest(Person):
    def __init__(self, name, age, sector, yoe, martial_Status):
        super().__init__(name, age, sector, yoe)
        self.martial_Status = martial_Status

    def pofdef(self):
        print(f"I'm {self.name} and my age is {self.age} {self.martial_Status}")


class Security(Person_of_interest):
    def __init__(self, name, age, sector, yoe, martial_Status, Weapon_of_choice):
        super().__init__(name, age, sector, yoe, martial_Status)
        self.Weapon_of_choice = Weapon_of_choice

    def security_weapon(self, name):
        print(f'{name} and the weapon of choice is {self.Weapon_of_choice}')


'''

emp1 = Person('james', 21, 'ml', 2)
emp3 = Manager('sam', 23, 'ml', 1)
print(emp3.duty())

emp4 = Person_of_interest('sfe',23,'ml', 3, 'unmarried')
print(emp4.pofdef())

'''
emp5 = Security('gane', 45, 'security', 6, 'M', 'fryer')
print(emp5.security_weapon('cobra'))

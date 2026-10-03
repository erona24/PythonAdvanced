from abc import ABC, abstractmethod


class Person(ABC):

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def check_condition(self):
        pass

    @abstractmethod
    def check_status(self):
        pass


class Adult(Person):

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def check_status(self):
        return "Adult"

    def check_condition(self):
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "Underweight"
        elif bmi < 24.9:
            return "Normal weight"
        elif bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"


class Child(Person):

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def check_status(self):
        return "Underage"

    def check_condition(self):
        bmi = self.calculate_bmi()

        if bmi < 14:
            return "Underweight"
        elif bmi < 18:
            return "Normal weight"
        elif bmi < 22:
            return "Overweight"
        else:
            return "Obese"


adult = Adult("Aurita", 24, 50, 1.78)

print("----- ADULT -----")
print("Name:", adult.name)
print("Age:", adult.age)
print("Weight:", adult.weight, "kg")
print("BMI:", round(adult.calculate_bmi(), 2))
print("Status:", adult.check_status())
print("Condition:", adult.check_condition())


child = Child("Esma", 12, 40, 1.50)

print("\n----- CHILD -----")
print("Name:", child.name)
print("Age:", child.age)
print("Weight:", child.weight, "kg")
print("BMI:", round(child.calculate_bmi(), 2))
print("Status:", child.check_status())
print("Condition:", child.check_condition())

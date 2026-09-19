class Dog:
    def __init__(self, name):
        self.name=name

    def sound(self):
        print(f"{self.name} makes the sound woof)

class Cat:

    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound mjau)

class Bird:

    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound ciu)

dog = Dog("husky")
cat = Cat("haiii")
bird = Bird("heyy")

for animal in (dog,cat,bird):
    animal.sound()


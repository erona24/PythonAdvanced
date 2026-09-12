class Studenti:

    def __init__(self, name, age, parentName, nivelin, pagesa):
        self.name=name
        self.age=age
        self.parentName=parentName
        self.nivelin=nivelin
        self.pagesa=pagesa

    def vjenNeOre(self):
        print( self.name + "ka marr pjes ne ore")

    def projektiPersonal(self):
        print("projekti final eshte i perfunduar")

    def pagesa(self):
        print(self.name + " ka edhe " + self.pagesa() + "borq")

    def kryerjaEPageses(self):
        self.pagesa() -40

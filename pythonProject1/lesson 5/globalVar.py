def sayHello():
    global mesazhi

    mesazhi = "Hi there!"
    return mesazhi

sayHello()
print(mesazhi)


def fullName():
    global name
    global lastname
    
    name = "erona"
    lastname = "krasniqi"
    return name+lastname

print(fullName())

print(name)
print(lastname)
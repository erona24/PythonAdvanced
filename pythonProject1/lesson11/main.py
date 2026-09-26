with open("test.txt","a") as file:
    file.write("\n haiii")

with open("test.txt","r") as file:
    content = file.read()
    print(content)

with open("test.txt","w") as file:
    file.write(content + " helloo")
# file  = open("example1.txt","r")
# content  = file.read()
#
# print("content")
#
# file.close()

with open("example2.txt","r") as file:
    content = file.read()
    print(content)

import os

with open("example2.txt","r") as file:
    content = file.read()
    print(content)

with open("example2.txt","a") as file:
    file.write("\nhello erona")

if os.path.exists("example2.txt"):
    print("file ekziston")
else:
    print("file nuk ekziston")
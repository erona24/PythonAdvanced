puntoret = {
    "Liza":3000,
    "Rudina":6000,
    "Lora":12000,
    "Erona":13000

}
print(puntoret["Erona"])

puntoret["Liza"]=14000

print(puntoret)

puntoret["Donjeta"]=5000

print(puntoret)

del puntoret["Lora"]

print(puntoret)

print(puntoret.keys())
print(puntoret.values())
print(puntoret.items())


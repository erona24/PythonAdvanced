#mblidhi te gjitha elementet
scores = [68,42,57,78,35,62,50]

shuma = 0

for i in scores:
    shuma = shuma+1

print(shuma)

for i in scores:
    if i ==57:
        continue
    shuma = shuma+1
print(shuma)

for i in scores:
    if i>35:
        shuma2=shuma2+1

print(shuma2)

import pandas as pd

produktet = ["Molla","Banane","Rrushi","Mango"]

sales = [150,200,180,190]

sales_series = pd.Series(sales, index=produktet)
print(sales_series)

print(sales_series["Mango"])

shitjetTotale = sales_series.sum()
print(shitjetTotale)

shitjaMaeMadhe = sales_series.idmax()
print(f"Shitje me se shumti ka pasur :{shitjaMaeMadhe}")
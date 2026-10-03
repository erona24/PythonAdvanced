import pandas as pd

data = {
    'Name':["Alice","Bob","Dua"],
    'age':[25,30,22],
    'city':['New York',"Prishtina","Peja"]
}

df = pd.DataFrame(data)
print(df)
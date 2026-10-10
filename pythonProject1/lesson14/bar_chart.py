import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data1.csv')

filtered_df = df[df['Average IQ'] >= 100]

filtered_df = filtered_df.sort_values(by="Average IQ", ascending=False)

print(filtered_df)

plt.figure(figsize=(14,8))

bars = plt.bar(filtered_df["Country"], filtered_df["Average IQ"], color="skyblue")

plt.title("Average Iq by Country")

plt.show()

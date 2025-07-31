import pandas as pd
import numpy as np
data = { "Name": ["Amit","Sagar","pooja"],     #to method for data csv mdhe pathvaycha
        "Math": [85,90,78],
        "Science": [92,88,80],
        "English": [75,85,82]
}

df = pd.DataFrame(data)
print("Data before strting")
print(df)

df["Total"] = df["Math"] + df["Science"] + df["English"]

df_new = df.sort_values(by="Total", ascending= False)

print("data after sorting")

print(df_new)
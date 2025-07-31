import pandas as pd
import numpy as np
data = { "Name": ["Amit","Sagar","pooja"],     #to method for data csv mdhe pathvaycha
        "Math": [85,90,78],
        "Science": [92,88,80],
        "English": [75,85,82]
}

df = pd.DataFrame(data)

print("Students who score mre than 85 in science ")

print(df[df["Science"]>85])
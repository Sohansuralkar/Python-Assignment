
import pandas as pd
import numpy as np
data = { "Name": ["Amit","Sagar","pooja"],     #to method for data csv mdhe pathvaycha
        "Math": [85,90,78],
        "Science": [92,88,80],
        "English": [75,85,82]
}

df = pd.DataFrame(data)
print("Output of describe method :")
print(df.describe())
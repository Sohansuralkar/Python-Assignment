import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = { "Name": ["Amit","Sagar","pooja"],     #to method for data csv mdhe pathvaycha
        "Math": [np.nan,90,78],
        "Science": [92,np.nan,85]

}

df = pd.DataFrame(data)
print(df)
df.fillna(df.mean(numeric_only=True),inplace=True)
print(df)

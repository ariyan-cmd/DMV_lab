import pandas as pd
import numpy as np

data = np.array([1, 2, np.nan, 4, np.nan])

df = pd.DataFrame(data, columns=["Values"])

print(df.isna())

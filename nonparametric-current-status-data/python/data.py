import numpy as np
import pandas as pd

a = np.arange(0,30)
b = np.arange(0,100)
a = np.array(pd.DataFrame(a).sample(n = 30 ,replace = False)).reshape(-1,1)
b = np.array(pd.DataFrame(b).sample(n = 30 ,replace = False)).reshape(-1,1)
a = np.hstack((a,b))


a = pd.DataFrame(a)
a.to_csv("data.csv",index=False,header=False)

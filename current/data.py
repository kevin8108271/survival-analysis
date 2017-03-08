import numpy as np
import pandas as pd

a = np.arange(30,500)
a = np.array(pd.DataFrame(a).sample(n = 70 ,replace = False)).reshape(-1,2)
a = a[a[:,0] >= a[:,1],:]
a = np.vstack((np.arange(len(a[0,:])),a))

a = pd.DataFrame(a)
a.to_csv("data.csv")

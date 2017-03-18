
# coding: utf-8

# In[161]:

import numpy as np
import pandas as pd
from numpy.linalg import inv


x_or = pd.read_csv('./lung.csv')
x_or = np.array(x_or)[:,1:]
x_or[x_or[:,2]==1,1] = x_or[x_or[:,2]==1,1]-0.05
x_or = x_or[np.argsort(x_or[:,1]),]                         ##排序
x_or = x_or[np.sum(np.isnan(x_or)*1,axis=1)==0,:]
number0 =np.shape( x_or[:,1])[0]

x_t = x_or[:,1]                                             ##time
x_c = x_or[:,2]
x_z = np.hstack((x_or[:,0].reshape(-1,1),x_or[:,3:]))       ##cov
iteration_max=100


coxph(x_t,x_z,x_c,iteration_max)


# In[160]:


def coxph(x_t,x_z,x_c,iteration_max):
    bu = np.zeros(8).reshape(-1,1)+0.001
    bc = np.zeros(8).reshape(-1,1)+0.001
    dls = np.zeros(8).reshape(8,1)
    ddls = np.zeros(64).reshape(8,8)
    for j in range(iteration_max):
        bc = bu

        dls = np.zeros(8).reshape(-1,1)
        for i in range(number0):
            if x_c[i]==1:continue
            temp = np.exp(np.dot(x_z[i:,:],bc)).reshape(-1,1)
            tempx = x_z[i:,].reshape(-1,8)
            tx = np.transpose(tempx)

            dls = dls + x_z[i,:].reshape(-1,1)-np.dot(tx,temp)/sum(temp)

        ddls = np.zeros(64).reshape(8,8)
        for i in range(number0):
            if x_c[i]==1:continue
            di = np.diagflat(np.exp(np.dot(x_z[i:,:],bc)))
            temp = np.exp(np.dot(x_z[i:,:],bc)).reshape(-1,1)
            tempx = x_z[i:,].reshape(-1,8)
            tx = np.transpose(tempx)

            ddls = ddls + np.dot(np.dot(tx,di),tempx)/sum(temp) - np.dot(np.dot(tx,temp),np.transpose(np.dot(tx,temp)))/sum(temp)/sum(temp)

        bu = bc + np.dot(inv(ddls),dls)
        if np.sum((np.abs(bu-bc)>(10**(-8)))*1)==0:
            print('iteration time=',j)
            break
        elif j == iteration_max-1:
            print('iteration up to max')
    print(bu)
    return(bu)


# In[126]:

coef exp(coef)  se(coef)     z       p
x[, 1]  -3.04e-02  9.70e-01  1.31e-02 -2.31 0.02062
x[, 4]   1.28e-02  1.01e+00  1.19e-02  1.07 0.28340
x[, 5]  -5.67e-01  5.67e-01  2.01e-01 -2.81 0.00489
x[, 6]   9.07e-01  2.48e+00  2.39e-01  3.80 0.00014
x[, 7]   2.66e-02  1.03e+00  1.16e-02  2.29 0.02223
x[, 8]  -1.09e-02  9.89e-01  8.14e-03 -1.34 0.18016
x[, 9]   2.60e-06  1.00e+00  2.68e-04  0.01 0.99224
x[, 10] -1.67e-02  9.83e-01  7.91e-03 -2.11 0.03465


# In[153]:

np.sum((np.abs(bu-bc)>(10**(-8)))*1)


# In[132]:

x_or[:,1:3]


# In[ ]:




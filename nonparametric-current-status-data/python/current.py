import numpy as np
import pandas as pd

data = np.array(pd.read_csv('./data.csv',names=['die','life']))
b = 0
l = len(data[:,0])

for j in range(l):

	m1 = np.repeat(0,l*(j+1)).reshape(l,j+1)
	m2 = np.repeat(0,(l-j+2)*l).reshape(l-j+2,l)
	m3 = np.repeat(0,(l-j+2)*l).reshape(l-j+2,l)
	
	for u in range(j+1):
		m1[u:l,u] = 1
	
	for v in range(l-j):  ##want to use j:len,how to produce?
		m2[v,0:(v+j+1)] = data[0:(v+j+1),0]
		m3[v,0:(v+j+1)] = data[0:(v+j+1),1]
	
	numerator = np.dot(m2,m1)
	denominator = np.dot(m2,m1)+np.dot(m3,m1)
	al = numerator/denominator
	
	a = 0
	for z in range(j+1):
		if(min(al[:,z])>a):a = min(al[:,z])

	if(j==0):cdf = np.array([a])
	else: cdf = np.vstack((cdf,a))

pd.DataFrame(cdf).to_csv('./result.csv',header = ['cdf'],index=False)

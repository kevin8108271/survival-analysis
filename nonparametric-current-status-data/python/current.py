import numpy as np
import pandas as pd
	
data = np.array(pd.read_csv('./data.csv'))
b = 0
cdf = np.array([0])
l = len(data[:,0])
for j in range(l):

	m1 = np.repeat(0,l*(j+1)).reshape(l,j+1)
	m2 = np.repeat(0,(l-j+2)*l).reshape(l-j+2,l)
	m3 = np.repeat(0,(l-j+2)*l).reshape(l-j+2,l)
	
	for u in range(j):
		m1[u:l,u] = 1
	
	for v in range(l-j+1):  ##want to use j:len,how to produce?
		m2[v,0:(v+j)] = data[0:(v+j),1]
		m3[v,0:(v+j)] = data[0:(v+j),2]
	
	numerator = np.dot(m2,m1)
	denominator = np.dot(m2,m1)+np.dot(m3,m1)
	al = numerator/denominator
	
	a = 0
	for z in range(j+1):
		if(min(al[:,z])>a):a=min(al[:,z])
	cdf=np.vstack((cdf,a))

pd.DataFrame(cdf[1:]).to_csv('./result.csv',header = ['cdf'],index=False)

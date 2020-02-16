import numpy as np
import matplotlib.pyplot as plt 
x= np.linspace(-2,1,4)
a = np.poly1d([1,3,7,9,1]) #coefficients of transfer function
c = a.c	
a = a.r
print(c)
print(a)
r = np.zeros((5,4))

try:
	for i in range(len(r[1])):
		r[0][i] = c[2*i]
except IndexError:
	print("-")

try:
	for i in range(len(r[1])):
		r[1][i] = c[2*i+1]
except IndexError:
	print("-")
for j in range(2,len(r)):	
	try:
		for i in range(len(r[i])):
			r[j][i] = (r[j-1][0]*r[j-2][i+1]-r[j-2][0]*r[j-1][i+1])/r[j-1][0]
	except IndexError:
		print("-")	
z = 0
for i in range(1,len(r)):
		if(r[i][0]<0):
			z = z + 1
print("ROUTH ARRAY FOR GIVEN TRANSFER FUNCTION IS:")
print(r)	
if(z > 0):
	print("SYSTEM IS NOT STABLE")
elif(z == 0):
	print("SYSTEM IS STABLE")			

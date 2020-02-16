import numpy as np
import matplotlib.pyplot as plt
import math as mp
from pylab import *
import cmath
m = np.array([])
w = np.linspace(0,10000,10001)
H = 100*(( (0+1j)*w)+1)/(((0+1j)*w)**2+110*(0+1j)*w+1000)
h = abs(H)
phase = np.array([])
for i in h:
	m = np.append(m,[20*mp.log(i)/mp.log(10)])
for k in H:
	phase = np.append(phase,[(np.degrees(cmath.phase(k)))])	
plt.semilogx(w,m)
plt.title("magnitude plot")
figure(2)
plt.semilogx(w,phase)
plt.title("phase plot")
plt.show()

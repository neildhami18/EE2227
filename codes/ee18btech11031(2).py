# Code by Neil
# Unit step response

import sympy as sp
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


A = np.array([
	[0,1],
	[-2,-3]
])

B = np.array([
	[0],
	[1]
])

C = np.array([
	[1,0]
])

D = 0
sys = signal.StateSpace(A,B,C,D) #State space to time domain conversion

t1,y1= signal.step2(sys) # time and output axis for natural(impulse) response


plt.plot(t1,y1,label='Unit step response')
plt.legend()
plt.grid()
plt.show()













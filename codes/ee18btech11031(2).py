# Code by Neil
# Unit step response


import numpy as np
import sympy as sp
from sympy.abc import s,t
from sympy.integrals import inverse_laplace_transform
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

Hs = 1/(s**2 + 3*s + 2) 

Us = 1/s

Ys = Hs * Us

#print(Ys)

y = inverse_laplace_transform(Ys,s,t)

print("Unit step response =",y) # Note: "Heaviside(t)" is nothing but u(t):unit step
plt.plot(t1,y1,label='Unit step response')
plt.legend()
plt.grid()
plt.show()













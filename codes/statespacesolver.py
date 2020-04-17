import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

A = np.array([
	[0.0,1.0],
	[-2.0,-3.0]
])

B = np.array([
	[0.0],
	[1.0]
])

C = np.array([
	[1.0,0.0]
])

D = 0.0

sys = signal.StateSpace(A,B,C,D)

t1,y1= signal.impulse2(sys)

plt.plot(t1,y1,label='impulse response')
plt.legend()
plt.grid()
plt.show()

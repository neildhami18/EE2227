import numpy as np
import matplotlib.pyplot as plt
import control

#values of omega (w)
OMEGA = np.linspace(-20, 20, 2001)

#defining transfer function
s = control.TransferFunction.s
G = 1/((s+1)*(s+2))

#Using library getting mag and phase of the transfer function for resp. omegas
MAG, PHASE, W = G.freqresp(OMEGA)




#plotting the polar plot
ax1 = plt.subplot(111, projection='polar')
ax1.plot(PHASE.reshape((2001,))[-1000:],MAG.reshape((2001,))[-1000:])
plt.polar(-np.pi,1,'o')
plt.text(-np.pi,1,'(-1,0)')
plt.title("polar plot")
plt.show()

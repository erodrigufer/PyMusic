'''
Reference script to perform a FFT of a discrete signal
https://scipy.github.io/devdocs/tutorial/fft.html

-> Stackoverflow reference:
https://stackoverflow.com/questions/25735153/plotting-a-fast-fourier-transform-in-python
'''
import numpy as np
import scipy

# Number of sample points
N = 600

# sample spacing
T = 1.0 / 800.0 # sample period
t = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*t) + 0.5*np.sin(80.0 * 2.0*np.pi*t)
yf = scipy.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2) 
# // is the operator for a floor division

import matplotlib.pyplot as plt
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()

import numpy as np
from numpy.fft import fft2
a2 = np.array([[100,200],[100,200]])
a2 = np.tile(a2,(4,4))
A2 = np.int16(fft2(a2))

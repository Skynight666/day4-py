import numpy as np
from skimage import io, exposure as ex,util as ut
import scipy.ndimage as ndi
from numpy.fft import fft2
from numpy.fft import ifft2
cr=io.imread('car.png')
m = np.ones((1,7))/7
cm = ndi.correlate(cr,m)

m2 = np.zeros_like(cr)*1.0
m2[0,0:7] = m
d = 0.02
mf = fft2(m2)
mf[np.where(abs(mf)<d)] = 1
bmi = abs(ifft2(fft2(cm)/mf))
bmu = ut.img_as_ubyte(bmi/bmi.max())
io.imshow(ex.rescale_intensity(bmu,in_range=(0,128)))

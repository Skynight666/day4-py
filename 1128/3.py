from numpy.fft import fft2, fftshift
import numpy as np
from skimage import io, exposure as ex
ar = np.arange(-128,128)
x,y = np.meshgrid(ar,ar)
z = np.sqrt(x**2+y**2)
c = (z<15)*1
cf = fftshift(fft2(c))
cfl = np.log(1+abs(cf))
c2 = 1/(1+(z/15)**2)
io.imshow(ex.rescale_intensity(c,out_range=(0.0,1.0)))


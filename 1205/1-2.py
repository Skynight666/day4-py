import skimage.io as io
import numpy as np
from numpy.fft import ifft2
from numpy.fft import fft2, fftshift
from skimage import io, exposure as ex
cm = io.imread('cameraman.png')
ar = range(-128,128)
x,y = np.meshgrid(ar,ar)
D = 15.0
bh = 1-1.0/(1.0+((x**2+y**2)/D**2)**2)
cf = fftshift(fft2(cm))
cfbh = cf*bh
io.imshow(ex.rescale_intensity(abs(ifft2(cfbh))))
io.imshow(np.log(1+abs(cfbh)),cmap='gray')
io.show()
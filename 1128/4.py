import skimage.io as io
import numpy as np
from numpy.fft import fft2, fftshift
from skimage import io, exposure as ex
cm = io.imread('cameraman.png')
cf = fftshift(fft2(cm))
cfl = np.log(1+abs(cf))
io.imshow(ex.rescale_intensity(cfl,out_range=(0.0,1.0)))

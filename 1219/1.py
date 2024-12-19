from skimage import io, exposure as ex,util as ut
import skimage.color as co
import numpy as np
import skimage
from numpy.fft import fft2, fftshift
from numpy.fft import ifft2
g = co.rgb2gray(io.imread('gull.png'))
r,c = g.shape
x,y = np.mgrid[0:r,0:c].astype('float32')
p = np.sin(x/3+y/5)+1.0
gp = (2*skimage.util.img_as_float(g)+p/2)/3
gf = fftshift(fft2(gp))
temp = ex.rescale_intensity(abs(gf),out_range=(0,1))
gf2 = ut.img_as_ubyte(temp)
gf2[200,200]=0
i,j=np.where(gf2==gf2.max())
gf2= np.copy(gf)
gf2[i,:] = 0
gf2[:,j] = 0
gf2i=ifft2(gf2)
io.imshow(np.log(1+abs(gf2)),cmap='gray')
io.show()
io.imshow(np.abs(gf2i), cmap='gray')
io.show()

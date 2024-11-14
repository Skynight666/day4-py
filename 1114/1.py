import skimage.io as io
from numpy import array
import scipy.ndimage as ndi
from numpy import float32
c = io.imread('cameraman.png')
f = array([[1,-2,1],[-2,4,-2],[1,-2,1]])
cf1 = ndi.convolve(c,f)
cf2 = ndi.convolve(float32(c),f,mode='constant')
maxcf2 = cf2.max()
mincf2 = cf1.min()
cf2f = (cf2-mincf2)/(maxcf2-mincf2)
io.imshow(cf2f)

io.imshow(cf2/60,vmax=1.0,vmin=0.0,cmap='gray')

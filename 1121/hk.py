import skimage.io as io
import scipy.ndimage as ndi
from numpy import float32
c = io.imread('cameraman.png')

cf2 = ndi.convolve(float32(c),f,mode='constant')
maxcf2 = cf2.max()
mincf2 = cf2.min()
cf2f = (cf2-mincf2)/(maxcf2-mincf2)
io.imshow(cf2f)
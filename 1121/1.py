import scipy.ndimage as ndi
from numpy import sqrt
from numpy import mean
import skimage.io as io

def rms(x):
    return sqrt(mean(x**2))

c = io.imread('cameraman.png')
cr = ndi.generic_filter(c,rms,size=(3,3))
io.imshow(cr)
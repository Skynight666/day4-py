from numpy import uint8
from numpy import array
from numpy import ones
import skimage.io as io
import scipy.ndimage as ndi
x = 10*uint8(array([[17,24,1,8,15],[23,5,7,14,16],\
                    [4,6,13,20,22],[10,12,19,21,3],[11,18,25,2,9]]))
a = ones((3,3))/9
y = ndi.convolve(x,a,mode='constant')
c = io.imread('cameraman.png')
cfa = ndi.convolve(c,ones((9,9))/81,mode='constant')
io.imshow(cfa)

cfb = ndi.unifrom_filter(c,[9,9],mode='constant')
cfb2 = ndi.unifrom_filter(c,[9,9])
cfc = ndi.unifrom_filter(c,25)
cfc = ndi.unifrom_filter(c,50)
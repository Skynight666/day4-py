import skimage.io as io
x = io.imread('thylacine.png')

from numpy import array
from numpy import uint8
import numpy as np
D = array([[0,128],[192,64]])
r = np.tile(D,(160,200))
x2 = (x > r).astype(uint8)
io.imshow(x2,cmap = 'gray')
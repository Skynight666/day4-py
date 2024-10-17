import skimage.io as io
b = io.imread('blocks.jpg')
io.imshow(b+128)
from numpy import uint8
import numpy as np
from numpy import float64
bf = float64(b)
b4 = uint8(np.clip(bf*2,0,255))
b5 = uint8(np.clip(bf/2+128,0,255))
io.imshow(b5)
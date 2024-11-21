import skimage.io as io
import numpy as np
from skimage.draw import polygon
import skimage.util as ut
import scipy.ndimage as fl

m2 = io.imread('monkey.png');m = m2[55:281,220:412]
r,c = m.shape

xi = np.array([60,27,14,78,130,139])
yi = np.array([14,38,127,177,160,69])
roi = np.zeros_like(m)
rr,cc=polygon(yi,xi)
roi[cc,rr] = 1

mg = ut.img_as_ubyte(fl.gaussian_filter(m,9))
mr = mg*roi + m*(1-roi)

io.imshow(m*(1-roi))
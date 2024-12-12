import skimage.io as io
import skimage.color as co
import numpy as np
import skimage
g = co.rgb2gray(io.imread('gull.png'))
r,c = g.shape
x,y = np.mgrid[0:r,0:c].astype('float32')
p = np.sin(x/3+y/3)+1.0
gp = (2*skimage.util.img_as_float(g)+p/2)/3
io.imshow(gp)
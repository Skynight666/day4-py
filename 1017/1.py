import skimage.io as io
x = io.imread('thylacine.png')

import skimage.transform as tr
x4 = tr.rescale(tr.rescale(x,0.25),4,order=0)
x16 = tr.rescale(tr.rescale(x,1/16),16,order=0)


io.imshow(x16)

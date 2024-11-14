import scipy.ndimage as ndi
import skimage.io as io
c = io.imread('cameraman.png')
cg1 = ndi.gaussian_filter(c,0.5,truncate=4.5)
cg2 = ndi.gaussian_filter(c,2,truncate=1)
cg3 = ndi.gaussian_filter(c,1,truncate=5)
cg4 = ndi.gaussian_filter(c,5,truncate=1)
io.imshow(cg4)

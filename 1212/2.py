import skimage.io as io
import skimage.color as co
import skimage.util.noise as noise
import scipy.ndimage as ndi
g = co.rgb2gray(io.imread('gull.png'))
gsp2 = noise.random_noise(g,mode='s&p',amount=0.2)
gm23 = ndi.median_filter(gsp2,3)
gm25 = ndi.median_filter(gsp2,5) 
io.imshow(gm25)
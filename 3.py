import skimage.io as io
import skimage.color as co
import skimage.util.noise as noise
from scipy.signal import wiener
g = co.rgb2gray(io.imread('gull.png'))
gg2 = noise.random_noise(g,mode='gaussian',mean=0,var=0.005)
gg2w = wiener(gg2,[7,7])
io.imshow(gg2w)
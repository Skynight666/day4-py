import skimage.util.noise as noise
import skimage.io as io
g = io.imread('gull_gray.png')
gn = noise.random_noise(g, mode='s&p')
gn2 = noise.random_noise(g, mode='s&p',amount=0.2)
io.imshow(gn2)
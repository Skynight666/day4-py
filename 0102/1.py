from skimage import io
import skimage.util.noise as noise
import skimage.color as co
import scipy.ndimage as ndi
import numpy as np
t = io.imread('twins.jpg')
tn = noise.random_noise(t,mode='s&p',amount=0.2)

tnm = np.zeros_like(tn)
for i in range(3):
    tnm[:,:,i] = ndi.median_filter(tn[:,:,i],3)

tnh = co.rgb2hsv(tn)
tnh[:,:,2] = ndi.median_filter(tnh[:,:,2],3)
tnm2 = co.hsv2rgb(tnh)
io.imshow(tnm)
from skimage import io ,exposure
import numpy as np
s = io.imread('color_sunset.png').astype('float64')
s2 = np.zeros_like(s)
for i in range(3):
    s2[:,:,i] = exposure.equalize_hist(s[:,:,i])

io.imshow(s2)
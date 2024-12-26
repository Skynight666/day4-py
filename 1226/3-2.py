from skimage import io,exposure
s = io.imread('color_sunset.png').astype('float64')

import skimage.color as co
sh = co.rgb2hsv(s)
sh[:,:,2] = exposure.equalize_hist(sh[:,:,2])
s3 = co.hsv2rgb(sh)
io.imshow(s3)
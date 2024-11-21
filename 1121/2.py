import skimage.io as io
import skimage.restoration as re

c = io.imread('cameraman.png')

cb = re.denoise_bilateral(c,win_size=5,sigma_color=0.2,\
                          sigma_spatial=2)
cb2 = re.denoise_bilateral(c,win_size=7,sigma_color=0.2,\
                          sigma_spatial=10)
cb3 = re.denoise_bilateral(c,win_size=11,sigma_color=0.1,\
                          sigma_spatial=3)
cb4 = re.denoise_bilateral(c,win_size=11,sigma_color=0.5,\
                          sigma_spatial=5)
    
io.imshow(cb)
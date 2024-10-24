import skimage.io as io
import skimage.exposure as ex
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
c = io.imread('chickens.png')
ca1 = ex.adjust_gamma(c,0.5)
ca2 = ex.adjust_gamma(c,0.25)
io.imshow(ca1)
f = figure()
f.show(plt.hist(ca1.flatten(),bins=256))
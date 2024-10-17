import skimage.io as io
c = io.imread('chickens.png')
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
io.imshow(c)
f = figure()
f.show(plt.hist(c.flatten(),bins=256))
io.imshow(f)
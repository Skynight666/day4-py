import skimage.io as io
import skimage.exposure as ex
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
c = io.imread('chickens.png')
ch = ex.equalize_hist(c)
f = figure();f.show(plt.hist(ch.flatten(),bins=256))
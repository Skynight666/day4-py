from skimage.morphology import binary_erosion as bwerode
from skimage import io
import matplotlib.pyplot as plt
from numpy import ones
r = io.imread('binary_tools.png')
sq = ones((3,3))
re = bwerode(r,sq)
f = plt.figure();
re2 = bwerode(re,sq);f.show(io.imshow(re2))

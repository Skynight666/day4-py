from skimage import io
from numpy import ones
import matplotlib.pyplot as plt
from skimage.morphology import binary_dilation as bwdilate
from skimage.morphology import binary_erosion as bwerode
n = io.imread('pinenuts.png')
p = ~((n>130)&(n<165))
sq = ones((3,3))
pe = bwerode(p,sq)
pd = bwdilate(p,sq)
p_exp = pd & (1-p)
p_grad = pd & (1-pe)
io.imshow(p_exp,cmap='gray')
f = plt.figure();f.show(io.imshow(p_grad,cmap='gray'))
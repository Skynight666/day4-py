from skimage import io
import numpy as np
from skimage.morphology import binary_closing as bwclose
t = io.imread('morph_text.png')
k = np.array([[0,0,0,0,1,1],[0,0,1,1,0,0],[1,1,0,0,0,0]])
tc = bwclose(t,k)
io.imshow(tc)
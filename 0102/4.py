from skimage import io
import numpy as np
from numpy import ones
from skimage.morphology import binary_closing as bwclose
from skimage.morphology import binary_opening as bwopen
c = io.imread('circles.png').astype('bool')*1
x = np.random.random_sample(c.shape)
c[np.nonzero(x>0.95)]=0
c[np.nonzero(x<=0.05)]=1

sq = ones((3,3))
cf1 = bwclose(bwopen(c,sq),sq)

cr = np.array([[0,1,0],[1,1,1],[0,1,0]])
cf2 = bwclose(bwopen(c,cr),cr)

io.imshow(cf2,cmap='gray')
import skimage.io as io
import matplotlib.pyplot as plt

x = io.imread('thylacine.png')

qs = [2**i for i in range(8)]
qSub = [x//qs[i]*qs[i]for i in range(8)]

io.imshow(qSub[4])
io.imshow(qSub[7])



import matplotlib.pyplot as plt
import numpy as np
nxyz = np.loadtxt('ciexyz31.txt',delimiter=',')
xyz = nxyz[:,1:]
sums = xyz.sum(axis=1)
newxyz = xyz/sums[:,np.newaxis]
x = newxyz[:,0];x1 = np.hstack((x,x[0]))
y = newxyz[:,1];y1 = np.hstack((y,y[0]))
plt.plot(x1,y1)
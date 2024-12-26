import numpy as np
import matplotlib.pyplot as plt

def plotgamut():
    xyz2rgb = np.array([[3.063,-1.393,-0.476],[-0.969,1.876,0.042],[0.068,-0.229,1.069]])
    ciexyz = np.loadtxt('ciexyz31.txt',delimiter=',')
    ciexyz1 = np.vstack((ciexyz,ciexyz[0,:,np.newaxis].T))
    W = ciexyz1[:,0]
    X = ciexyz1[:,1]
    Y = ciexyz1[:,2]
    Z = ciexyz1[:,3]
    S = X+Y+Z
    
    xx,yy=np.mgrid[0:512,0:512].astype('float64')
    z0 = np.zeros((512,512,3))
    z0[:,:,0]=xx/512
    z0[:,:,1]=yy/512
    z0[:,:,2]=1.0-xx/512-yy/512
    z0r = np.reshape(z0,(xx.size,3),order='C').T
    rgb0 = xyz2rgb.dot(z0r)
    mn = (rgb0.min(axis=0)<0)*1.0
    rgb1 = np.maximum(rgb0,np.tile(mn,(3,1)))
    
    rgbs = np.reshape(rgb1.T,(xx.shape+(3,)),order='F');
    rgbs[np.where(rgbs>1)]=1.0
    
    plt.plot(np.ceil(X/S*512),512-np.ceil(Y/S*512))
    plt.imshow(np.flipud(rgbs),aspect='equal',origin='upper')
    plt.show()
    
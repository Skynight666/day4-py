import numpy as np
from numpy import arange
import skimage.io as io

def homfilt(im,cutoff,order,lowgain,highgain):
    from scipy.fftpack import fft2,ifft2,fftshift
    u = im.astype('uint8')
    u[np.where(u==0)]==1
    lg = np.log(u.astype(float))
    ft = fftshift(fft2(lg))
    rows,cols = im.shape
    rr = arange(-(rows//2),(rows+1)//2,1.0)
    cr = arange(-(cols//2),(cols+1)//2,1.0)
    y,x = np.meshgrid(cr,rr)
    bl = 1.0/(1.0+0.414*((x*x+y*y)/cutoff**2)**order)
    f = lowgain+(highgain-lowgain)*(1.0-bl)
    b = f*ft
    ib = abs(ifft2(b))
    return np.exp(ib)

a=io.imread('arch.png')
ah = homfilt(a,128,2,0.5,2);
io.imshow(ah,vmax=12,cmap='gray')
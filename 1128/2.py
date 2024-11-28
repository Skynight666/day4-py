from numpy.fft import fft2, fftshift
import numpy as np
from skimage import io, exposure as ex
from matplotlib import pyplot as plt
x, y = np.meshgrid(range(256), range(256))
b = (x + y < 329) & (x + y > 182) & (x - y > -67) & (x - y < 73)
io.imshow(b)
bf = fftshift(fft2(b))
bfl = np.log(1 + np.abs(bf))
io.imshow(ex.rescale_intensity(bfl, out_range=(0.0, 1.0)))
plt.show()

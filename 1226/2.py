from skimage import io
import matplotlib.pyplot as plt
x = io.imread('twins.jpg')
x.shape
for i in range(3):
    plt.figure(i+2);io.imshow(x[:,:,i])

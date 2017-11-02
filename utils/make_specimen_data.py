import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

n = 5
dim = 512
l = 400


for i in range(50):
    im = np.zeros((dim, dim))
    points = l*np.random.random((2, n**2))
    points += (dim-l)/2

    im[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1

    plt.subplot(121)
    plt.imshow(im, cmap=plt.cm.gray)
    plt.subplot(122)
    im = ndimage.gaussian_filter(im, sigma=dim/(10.*n))
    mask = im > im.mean()
    mask = np.array(mask, dtype=int)
    plt.imshow(mask, cmap=plt.cm.gray)
    np.savetxt('{:02d}.txt'.format(i), mask, delimiter=',', fmt="%d")

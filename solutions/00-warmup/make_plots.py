import numpy as np
import matplotlib.pyplot as plt

plt.imshow(np.loadtxt('01.txt', delimiter=','), cmap=plt.cm.gray)
plt.savefig('01.png')

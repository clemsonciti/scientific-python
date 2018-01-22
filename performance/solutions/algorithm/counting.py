import numpy as np

def external_match(a):
    if np.sum(a) == 1:
            return True
    return False

def internal_match(a):
    if np.sum(a) == 3:
            return True
    return False
    
def count_objects(img):
    ny, nx = img.shape
    E = 0
    I = 0
    for i in range(ny-1):
        for j in range(nx-1):
            if external_match(img[i:i+2, j:j+2]):
                E += 1
            if internal_match(img[i:i+2, j:j+2]):
                I += 1
    return (E - I)/4

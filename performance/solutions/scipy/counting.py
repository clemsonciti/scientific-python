import numpy as np
import scipy.ndimage

def external_matches(img):
    masks = [np.array([[0, 0], [0, 1]]),
             np.array([[0, 0], [1, 0]]),
             np.array([[1, 0], [0, 0]]),
             np.array([[0, 1], [0, 0]])]
    
    matches = 0
    for mask in masks:
        matches += np.sum(
                scipy.ndimage.binary_hit_or_miss(img, mask, origin1=(-1, -1)))
    return matches

def internal_matches(img):
    masks = [np.array([[1, 1], [1, 0]]),
             np.array([[1, 1], [0, 1]]),
             np.array([[0, 1], [1, 1]]),
             np.array([[1, 0], [1, 1]])]
 
    matches = 0
    for mask in masks:
        matches += np.sum(
                scipy.ndimage.binary_hit_or_miss(img, mask, origin1=(-1, -1)))
    return matches

def count_objects(img):
    E = external_matches(img)
    I = internal_matches(img)
    return (E - I)/4

import numpy as np
import scipy.ndimage

def count_objects(img):
    label, num_features = scipy.ndimage.measurements.label(img)
    return num_features
    

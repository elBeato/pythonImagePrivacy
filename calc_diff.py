import numpy as np
import math
import cv2


def scale_and_convert(original, modified):
    # if the image is color, convert to grayscale
    if len(original.shape) == 3:
        original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
        modified = cv2.cvtColor(modified, cv2.COLOR_BGR2GRAY)

    # convert to float arrays
    original_flt = original.astype(float)
    modified_flt = modified.astype(float)

    # scale the intensity such that the average pixel has intensity 1
    original_average_intensity = np.sum(original_flt)/original_flt.size
    modified_average_intensity = np.sum(modified_flt)/modified_flt.size
    original_flt = original_flt / original_average_intensity
    modified_flt = modified_flt / modified_average_intensity

    return original_flt, modified_flt


def rms(original, modified):
    # calculate pixelwise rootmeansquare difference
    # between original and modified image
    original, modified = scale_and_convert(original, modified)
    difference = original - modified
    difference_squared = np.multiply(difference, difference)
    error = math.sqrt(np.sum(difference_squared)/difference_squared.size)
    return error

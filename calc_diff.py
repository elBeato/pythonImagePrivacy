import numpy as np
import math
import cv2


def convert(original, modified):

    # if the image is color, convert to grayscale
    if len(original.shape) == 3:
        original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
        modified = cv2.cvtColor(modified, cv2.COLOR_BGR2GRAY)

    # convert to float
    original = original.astype(np.float32)
    modified = modified.astype(np.float32)

    return original, modified


def diffvector(original, modified, space):

    # calculate difference vector between original and
    # modified image in chosen space
    if space == "image":
        difference = original - modified
    elif space == "histogram":
        hist_orig = cv2.calcHist([original], [0], None, [256], [0, 256])
        hist_modif = cv2.calcHist([modified], [0], None, [256], [0, 256])
        difference = hist_orig - hist_modif
    else:
        difference = 0

    return difference


def rms(original, modified, space="image"):

    '''
    this function calculates the rms error between two images

    the error calculation can either be done in image space or in histogram space

    output is scaled relative to the average input values

    output can be interpreted as a measure how much information was changed globally
    '''
    # convert image to grayscale and float
    original, modified = convert(original, modified)

    # calculate difference vector
    difference = diffvector(original, modified, space)

    # scale difference
    if space == "image":
        scale = np.sum(original) / original.size
        difference = difference / scale
    if space == "histogram":
        hist_orig = cv2.calcHist([original], [0], None, [256], [0, 256])
        scale = np.sum(hist_orig) / hist_orig.size
        difference = difference / scale

    # calculate rootmeansquare difference
    difference_squared = np.multiply(difference, difference)
    rms_error = math.sqrt(np.sum(difference_squared)/difference_squared.size)

    return rms_error


def chebyshev(original, modified, space="image"):

    '''
    this function calculates the maximal difference between two images

    the calculation can be done either in image space or in histogram space

    output is scaled relative to the input value

    output can be interpreted as a measure how much information was changed locally
    '''
    # convert image to grayscale and float
    original, modified = convert(original, modified)

    # calculate difference vector
    difference = abs(diffvector(original, modified, space))

    # calculate chebyshev distance and where it occurs
    max_diff = np.amax(difference)
    max_diff_ind = np.unravel_index(np.argmax(difference, axis=None), difference.shape)

    # scale difference
    if space == "image":
        scale = original[max_diff_ind]
        chebyshev_error = max_diff / scale
    if space == "histogram":
        hist_orig = cv2.calcHist([original], [0], None, [256], [0, 256])
        scale = hist_orig[max_diff_ind]
        chebyshev_error = max_diff / scale

    return chebyshev_error


def binary(original, modified, space="image"):

    '''
    this function calculates the percentage of pixels that have changed

    the calculation can be done either in image space or in histogram space

    output can be interpreted as a measure of how homogenous/inhomogenous
    the image changes are.

    output close to 1 means homogenous, close to 0 means inhomogenous
    '''
    # convert image to grayscale and float
    original, modified = convert(original, modified)

    # calculate difference vector
    difference = diffvector(original, modified, space)

    # calculate number of altered pixels
    nonzeros = np.count_nonzero(difference)

    return nonzeros / difference.size

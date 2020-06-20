# sharpen image using numpy convolution
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# convolution 2D function
def convolution2d(image, kernel, bias):
    m, n = kernel.shape
    if (m == n):
        y, x = image.shape
        y = y - m + 1
        x = x - m + 1
        new = np.zeros((y,x))
        for i in range(y):
            for j in range(x):
                new[i,j] = np.sum(image[i:i+m, j:j+m]*kernel) + bias
    return new

# Write your python program here

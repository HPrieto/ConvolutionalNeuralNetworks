import numpy as np
from scipy import signal

def pad_image(image,filter):
    """
        image: matrix image representation of size (n,n)
        filter: matrix filter for convolving
    """
    image_n = len(image)
    filter_n = len(filter)
    padding_n = int((filter_n - 1) / 2)
    padded_n = image_n + (padding_n*2)
    padded_image = np.zeros((padded_n,padded_n))
    for i in range(padding_n,(padding_n+image_n)):
        for j in range(padding_n,(padding_n+image_n)):
            padded_image[i][j] = image[i-padding_n][j-padding_n]
    return padded_image

# image matrix representation
image = np.array([[10,10,10,0,0,0],
                  [10,10,10,0,0,0],
                  [10,10,10,0,0,0],
                  [10,10,10,0,0,0],
                  [10,10,10,0,0,0],
                  [10,10,10,0,0,0]])
# basic filter
filter = np.array([[1,0,-1],
                   [1,0,-1],
                   [1,0,-1]])

pad_image(image,filter)

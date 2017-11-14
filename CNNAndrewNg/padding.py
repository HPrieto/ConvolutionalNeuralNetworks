import numpy as np
from scipy import signal

def pad_image(image,filter):
    """
        image: matrix image representation of size (n,n)
        filter: matrix filter for convolving
    """
    # image width
    image_n = len(image)
    # image height
    image_m = len(image[0])
    # filter width
    filter_n = len(filter)
    # filter height
    filter_m = len(filter[0])
    # padding needed for width
    padding_n = int((filter_n - 1) / 2)
    # padding needed for height
    padding_m = int((filter_m - 1) / 2)
    # new padded image width
    padded_n = image_n + (padding_n * 2)
    # new padded image height
    padded_m = image_m + (padding_m * 2)
    # new padded image matrix representation
    padded_image = np.zeros((padded_n,padded_m))
    for i in range(padding_n,(padding_n+image_n)):
        for j in range(padding_m,(padding_m+image_m)):
            padded_image[i][j] = image[i-padding_n][j-padding_m]
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

padded_image = pad_image(image,filter)
print('Image after padding:')
print(padded_image)

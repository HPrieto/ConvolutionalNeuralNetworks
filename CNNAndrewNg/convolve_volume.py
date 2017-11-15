import numpy as np
from scipy import signal

def convolve_3d(image,filter):
    """
    image: matrix image representation of (nxm) dimension
    filter: matrix filter representation of (sxs) dimension
    """
    dimensions = len(image)
    # image red values length and width
    r_n = len(image[0])
    r_m = len(image[0][0])
    # image green values length and width
    g_n = len(image[1])
    g_m = len(image[1][0])
    # image blue values length and width
    b_n = len(image[2])
    b_m = len(image[2][0])
    # filter for red image values
    fr_n = len(filter[0])
    fr_m = len(filter[0][0])
    # filter for green image values
    fg_n = len(filter[1])
    fg_m = len(filter[1][0])
    # filter for blue image values
    fb_n = len(filter[2])
    fb_m = len(filter[2][0])
    # convolution result matrix
    conv_n = r_n - fr_n + 1
    conv_m = r_m - fr_m + 1
    conv_result = np.zeros((conv_n,conv_m))
    for i in range(dimensions):
        result = signal.convolve2d(image[i],filter[i],mode='same',boundary='symm')
        print(result)

# RGB image matrix representation
imageRGB = np.array([[[10,10,10,0,0,0],# Red Values
                      [10,10,10,0,0,0],
                      [10,10,10,0,0,0],
                      [10,10,10,0,0,0],
                      [10,10,10,0,0,0],
                      [10,10,10,0,0,0]],
                      [[0,0,0,10,10,10],# Green Values
                       [0,0,0,10,10,10],
                       [0,0,0,10,10,10],
                       [0,0,0,10,10,10],
                       [0,0,0,10,10,10],
                       [0,0,0,10,10,10]],
                      [[0,0,0,0,0,0],# Blue Values
                       [0,0,0,0,0,0],
                       [0,0,0,0,0,0],
                       [10,10,10,10,10,10],
                       [10,10,10,10,10,10],
                       [10,10,10,10,10,10]]])
# basic filter
filter = np.array([[[1,0,-1],
                    [1,0,-1],
                    [1,0,-1]],
                   [[-1,0,1],
                    [-1,0,1],
                    [-1,0,1]],
                   [[1,1,1],
                    [0,0,0],
                    [-1,-1,-1]]])

# perform convolution
print(convolve_3d(imageRGB,filter));

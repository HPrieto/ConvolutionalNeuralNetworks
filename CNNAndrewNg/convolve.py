import numpy as np
from scipy import signal

image = np.array([[10,10,10,0,0,0],
                  [10,10,10,0,0,0],
                  [10,10,10,0,0,0],
                  [10,10,10,0,0,0],
                  [10,10,10,0,0,0],
                  [10,10,10,0,0,0]])

# basic filter
v_kluster = np.array([[1,0,-1],
                      [1,0,-1],
                      [1,0,-1]])
print("image: ")
print(image)

print('\n\nv_kluster :')
print(v_kluster)

v_conved = signal.convolve2d(image,v_kluster ,mode='same',boundary='symm')
print('\n\nv_convolved:')
print(v_conved)

# Sobel filter
sobel_filter = np.array([[1, 0, -1],
                         [2, 0, -2],
                         [1, 0, -1]])

sobel_filter_convolved = signal.convolve2d(image,sobel_filter,mode='same',boundary='symm')
print('Sobel Filter result:')
print(sobel_filter_convolved)

# Scharr filter
scharr_filter = np.array([[3,0,-3],
                          [10,0,-10],
                          [3,0,-3]])

scharr_filter_convolved = signal.convolve2d(image,scharr_filter,mode='same',boundary='symm')
print('Scharr Filter result:')
print(scharr_filter_convolved)

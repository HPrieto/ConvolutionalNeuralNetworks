import numpy as np
from scipy import signal

image = np.array([[10,10,10,0,0,0],
                  [10,10,10,0,0,0],
                  [10,10,10,0,0,0],
                  [10,10,10,0,0,0],
                  [10,10,10,0,0,0],
                  [10,10,10,0,0,0]])

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

h_image = np.array([[0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [10,10,10,10,10,10],
                    [10,10,10,10,10,10],
                    [10,10,10,10,10,10]])
print('\n\nimage with horizontal lines:')
print(h_image)

h_kluster = np.array([[1,1,1],
                   [0,0,0],
                   [-1,-1,-1]])
print('\n\nh_kluster:')
print(h_kluster)

h_convolved = signal.convolve2d(h_image,h_kluster,mode='same',boundary='symm')

print('\n\nh_convolved:')
print(h_convolved)

import numpy as np
from scipy import signal

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

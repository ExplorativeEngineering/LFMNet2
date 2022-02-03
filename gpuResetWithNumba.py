# pip install numba 

from numba import cuda 
device = cuda.get_current_device()
device.reset()
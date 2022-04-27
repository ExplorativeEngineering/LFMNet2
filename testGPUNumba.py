# pip install numba 

from numba import cuda 
device = cuda.get_current_device()
print("CUDA device: ", device)
#device.reset()
exit
# pip install numba
# conda install numba
# conda install cudatoolkit
import numba
print(numba.__version__)
from numba import jit
import numpy as np
from timeit import default_timer as timer
# To run on CPU
def func(a):
    for i in range(10000000):
        a[i]+= 1
# To run on GPU
@jit
def func2(x):
    return x+1
if __name__=="__main__":
    n = 10000000
    a = np.ones(n, dtype = np.float64)
    start = timer()
    func(a)
    print("without GPU:", timer()-start)
    start = timer()
    func2(a)
    numba.cuda.profile_stop()
    print("with GPU:", timer()-start)

import GPUtils

# nvidia-smi
# is CUDA toolkit installed?
# nvcc --version
# pip install numba
# conda install numba & conda install cudatoolkit
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

    # https://cupy.dev/

# https://github.com/anderskm/gputil
import GPUtil
deviceIDs = GPUtil.getAvailable(order = 'first', limit = 1, maxLoad = 0.5, maxMemory = 0.5, 
includeNan=False, excludeID=[], excludeUUID=[])
GPUtil.showUtilization(all=False, attrList=None, useOldCode=False)
GPUs = GPUtil.getGPUs()
GPUavailability = GPUtil.getAvailability(GPUs, maxLoad = 0.5, maxMemory = 0.5, includeNan=False, excludeID=[], excludeUUID=[])
# Get the first available GPU
DEVICE_ID_LIST = GPUtil.getFirstAvailable()
DEVICE_ID = DEVICE_ID_LIST[0] # grab first element from list
    
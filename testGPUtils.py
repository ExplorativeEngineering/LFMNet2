import GPUtil

# nvidia-smi
# is CUDA toolkit installed?
# nvcc --version

    # https://cupy.dev/

# https://github.com/anderskm/gputil
deviceIDs = GPUtil.getAvailable(order = 'first', limit = 1, maxLoad = 0.5, maxMemory = 0.5, includeNan=False, excludeID=[], excludeUUID=[])
GPUtil.showUtilization(all=False, attrList=None, useOldCode=False)
GPUs = GPUtil.getGPUs()
GPUavailability = GPUtil.getAvailability(GPUs, maxLoad = 0.5, maxMemory = 0.5, includeNan=False, excludeID=[], excludeUUID=[])
# Get the first available GPU
DEVICE_ID_LIST = GPUtil.getFirstAvailable()
DEVICE_ID = DEVICE_ID_LIST[0] # grab first element from list
    
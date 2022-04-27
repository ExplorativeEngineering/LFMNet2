# testCUDA.py
from __future__ import print_function
import torch

x = torch.rand(5, 3)
print(x)
print(torch.cuda.device_count())


if torch.cuda.is_available():
   print ("Cuda is available")
   device_id = torch.cuda.current_device()
   gpu_properties = torch.cuda.get_device_properties(device_id)
   print("Found %d GPUs available. Using GPU %d (%s) of compute capability %d.%d with "
          "%.1fGb total memory.\n" % 
          (torch.cuda.device_count(),
          device_id,
          gpu_properties.name,
          gpu_properties.major,
          gpu_properties.minor,
          gpu_properties.total_memory / 1e9))
else:    
   print ("Cuda is not available")
# from mainEval
   #  # Select GPUs to use
   #  argsTest.GPUs = list(range(torch.cuda.device_count())) if argsTest.GPUs is None else argsTest.GPUs
   #  print('Using GPUs: ' + str(argsTest.GPUs))
   #  # set Device to use
   #  device = torch.device("cuda:"+str(argsTest.GPUs[0]) if torch.cuda.is_available() else "cpu")
# Used retrieve GPU statistics
# GPUtil only works on Nvidia cards due to its reliance on nvidia-smi utility.
# Had to create a folder called NVSMI under C:\Program Files\NVIDIA Corporation, and
# I had to add these files nvidia-smi.exe and nvml.dll files under C:\Windows\System32 to the NVSMI folder.
#
# Michael Ashby
# Start:    3/5/2021
# Updated:  3/16/2022

import psutil
import GPUtil
import math


# Declaring and initializating string variables holding gpu statistics.
gpuName = None
driverVerison = None
driverDate = None
gpuTemperature = None
gpuUtilization = None
gpuSharedMemory = None
gpuDedicatedMemory = None
gpuObjs = []

# Holds number of requirements to display.
StatisticCount = 7

# Initialized an array of Strings holding the labels for the GPU data pulled. 
LabelTuple = ("GPU Name:  ", "Driver Verison:  ", "Driver Date:  ", "GPU Temperature:  ", "GPU Utilization:  ", "GPU Shared Memory:  ", "GPU Dedicated Memory:  ")

# Initialized an array of Strings holding the variables for the GPU.
VariableTuple = (gpuName, driverVerison, driverDate, gpuTemperature, gpuUtilization, gpuSharedMemory, gpuDedicatedMemory)

try:
  gpuObjs = GPUtil.getGPUs()
except Exception:
  print("Failed to retrieve GPUs.")

# Working on pulling parameters from the GPUtil object.
print (gpuObjs)

for gpuObj in gpuObjs:
  gpuName = gpuObj.name
  driverVerison = gpuObj.driver
  # driverDate = gpuObj.
  # gpuTemperature = gpuData.
  gpuUtilization = gpuObj.load
  # gpuSharedMemory = gpuObj.
  # gpuDedicatedMemory = 

# Try printing left and right column, catch an Exception for debugging.  
try:
    for y in range(StatisticCount):
      print(LabelTuple[y])
      print(VariableTuple[y])    
except FileNotFoundError:
    print("Error parsing and printing GPU information")
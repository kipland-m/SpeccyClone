# A method to retrieve GPU statistics
#
# gpu_info method
#
# Michael Ashby
# Start:    3/5/2021
# Updated:  2/16/2022

import psutil
import GPUtil
import math


#Declaring and initializating string variables holding gpu statistics.
gpuName = None
driverVerison = None
driverDate = None
gpuTemperature = None
gpuUtilization = None
gpuSharedMemory = None
gpuDedicatedMemory = None
gpuMainHead = None

StatisticCount = 7

gpuMainHead = GPUtil.getGPUs()
gpuName = gpuMainHead.name

# Initialized an array of Strings holding the labels for the GPU data pulled. 
Column1Tuple = ("GPU Name:  ", "Driver Verison:  ", "Driver Date:  ", "GPU Temperature:  ", "GPU Utilization:  ", "GPU Shared Memory:  ", "GPU Dedicated Memory:  ")

# Initialized an array of Strings holding the data for the GPU.
Column2Tuple = ()

#Try printing left and right column, catch an Exception for debugging.  
try:
    #Need functions returning values for each variable initialized in lines 14-20

    #Loop through the tuple and print its corresponding string
    for y in range(StatisticCount):
      
      #Print the correlating Drive Name
      print(Column1Tuple[y])
      #print(Column2Tuple[y])
        
except FileNotFoundError:
    print("Error parsing and printing GPU information")
# A method to retrieve Storage device statistics
#
# Drive_Info method
#
# Michael Ashby
# 3/2/2021


import psutil
import math

#Pulled this conversion formula from stackoverflow to convert disk_usage()'s output from bytes to a more coherent unit of measure.
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

#Set string to the drive you are analyzing. Need to add a for loop to check each available drive connected next time.
driveName='D:'

#Set tuple to hold data pulled when calling disk_usage 
temp=psutil.disk_usage(driveName)

#Set an array of Strings to the corresponding drive info printed
driveUsageStrings = ["Total  : ", "Used   : ", "Free   : ", "% Used : "]

#Loop through the tuple and print its corresponding string
for x in range(len(temp)):
  if x < 3 : print((driveUsageStrings[x]), convert_size(temp[x]))
  else : print((driveUsageStrings[x]),(temp[x]))
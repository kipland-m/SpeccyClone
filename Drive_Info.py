# A method to retrieve Storage device statistics
#
# drive_info method
#
# Michael Ashby
# Start:    3/2/2021
# Updated:  3/5/2021

import psutil
import math

#Conversion formula to convert disk_usage()'s output from bytes to a more comprehensible unit of measure.
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

#Tuple of possible drive letters.
driveName = ('A:', 'B:', 'C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:','N:','O:','P:','Q:','R:','S:','T:','U:','V:','W:','X:','Y:','Z:')

print()

#Loop through tuple of drive letters.
for x in range(len(driveName)):

  #Try parsing driveUseageStr, catch an Exception when driveUsageStr is empty. driveUsageStr is empty when passing an unmapped drive letter(i.e, driveName[x]=='Z:') to psutil. 
  try:
    driveUsageStr=psutil.disk_usage(driveName[x])

    #Set an array of Strings to the corresponding drive info printed. This gives us our left column.
    Column1Tuple = (driveName[x], "Total  : ", "Used   : ", "Free   : ", "Usage  : ")
    
    #Loop through the tuple and print its corresponding string
    for y in range(len(driveUsageStr)):
      
      #Print the correlating Drive Name
      if y == 0 : print(Column1Tuple[y])
           
      #Print the left column titles, data, and its unit of measure.
      if y < (3) :
        print(Column1Tuple[y+1], convert_size(driveUsageStr[y]))
      else :  print(Column1Tuple[y+1],driveUsageStr[y]," %")
    else : print()
  except FileNotFoundError:
    continue